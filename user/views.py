from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as loginn
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import event,tag
from .filter import eventFilter
from django.db.models import Count
from django.template.defaultfilters import date
from django.core.paginator import Paginator
import json
from django.core.cache import cache  # Import the cache method
from django.db.models.functions import ExtractYear




def home(request):
    
    queryset = event.objects.order_by('-event_date')
    sort_input = "default"
    if request.method == 'POST':
        sort_input =request.POST.get('selected_sort')
        if sort_input == "name-asc":
            queryset = event.objects.order_by('event_date') 
        else:
            queryset = event.objects.order_by('-event_date')
            
    # search_filter= eventFilter(request.GET,queryset=queryset)
    # queryset_filtered=search_filter.qs.distinct()
    # print(queryset)
    years = queryset.values('event_date__year')
    year_list = sorted(set(year['event_date__year'] for year in years), reverse=True)
    tag_list = tag.objects.all()

    title_filter=request.POST.get('headline')
    year_filter=request.POST.get('Year')
    month_filter=request.POST.get('month')
    day_filter=request.POST.get('day')
    tag_filter=request.POST.get('tag')

    if title_filter:
        queryset=queryset.filter(event_title__icontains=title_filter)
    if year_filter:
        year_filter = int(year_filter)
        queryset = queryset.filter(event_date__year=year_filter)
    if month_filter:
        queryset=queryset.filter(event_date__month=month_filter)
    if day_filter:
        day_filter = int(day_filter)
        queryset=queryset.filter(event_date__day=day_filter)
    print(queryset.values('event_date'))
    # if tag_filter:
    #     queryset=queryset.filter(tags__tag=tag_filter)
    grouped_queryset = queryset.values('event_date').annotate(count=Count('id'))
    paginator = Paginator(grouped_queryset, 10)  # Display 10 items per page
    page = request.GET.get('page')
    grouped_queryset_paginated = paginator.get_page(page)


    context = {'grouped_queryset': grouped_queryset_paginated, "queryset": queryset, 'events_num': len(queryset), 'paginator': paginator, 'sort_input': sort_input,"year_list":year_list,"year":year_filter,"month":month_filter,"day":day_filter,"title":title_filter,"tag":tag_filter,"tag_list":tag_list}

    return render(request, 'index.html', context)




def about(request):

    return render(request,'about.html')


def sort(request):


    if request.method == 'POST':
        sort_input=request.POST.get('input')

        json_data = json.dumps({'sort_input': sort_input,})



        return render(request,'index.html')

