from django.contrib import admin

# Register your models here.
from .models import Job, Apply

admin.site.register(Job)
admin.site.register(Apply)