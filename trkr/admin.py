from django.contrib import admin
from .models import Client, Activity, Exercise

class ClientList(admin.ModelAdmin):
    list_display = ('name', 'nick_name', 'cell_phone')
    list_filter = ('name', 'nick_name')
    search_fields = ('name', 'nick_name')
    ordering = ['name']

class ActivityList(admin.ModelAdmin):
    list_display = ('client', 'date', 'type')
    list_filter = ('client', 'date')
    search_fields = ('client', 'date')
    ordering = ['client']

class ExerciseList(admin.ModelAdmin):
    list_display = ('id', 'name', 'cal_minute', 'note')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name', 'note')
    ordering = ['name']


admin.site.register(Client, ClientList)
admin.site.register(Exercise, ExerciseList)
admin.site.register(Activity, ActivityList)
