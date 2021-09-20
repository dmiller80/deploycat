from django.contrib import admin
from .models import Client, Activity, Exercise

class ClientList(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'nick_name', 'cell_phone')
    list_filter = ('client_id', 'name')
    search_fields = ('client_id', 'name')
    ordering = ['client_id']

class ActivityList(admin.ModelAdmin):
    list_display = ('client', 'date', 'type')
    list_filter = ('client', 'date')
    search_fields = ('client', 'date')
    ordering = ['client']

class ExerciseList(admin.ModelAdmin):
    list_display = ('exercise_id', 'name', 'cal_minute', 'note')
    list_filter = ('exercise_id', 'name')
    search_fields = ('exercise_id', 'name', 'note')
    ordering = ['exercise_id']


admin.site.register(Client, ClientList)
admin.site.register(Exercise, ExerciseList)
admin.site.register(Activity, ActivityList)
