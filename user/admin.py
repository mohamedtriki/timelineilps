from django.contrib import admin
from .models import event
from .models import tag
from .models import excel_file


# Register your models here.
admin.site.register(event)
admin.site.register(tag)
admin.site.register(excel_file)