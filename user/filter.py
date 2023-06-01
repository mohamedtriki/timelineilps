import django_filters
from .models import event,tag
from django.forms.widgets import Select
from django_filters.filters import ModelMultipleChoiceFilter


class eventFilter(django_filters.FilterSet):
    # event_title = django_filters.CharFilter(lookup_expr='iexact')
    tags = ModelMultipleChoiceFilter(
        queryset=tag.objects.all(),
        widget=Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = event
        fields = ["event_title", 'event_date', 'tags', 'category']