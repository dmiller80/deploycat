from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from django.urls import path, re_path

app_name = 'trkr'
urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
    path('', TemplateView.as_view(template_name="trkr/home.html"), name='home'),
    path('client_list', views.client_list, name='client_list'),
    path('client/create/', views.client_new, name='client_new'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('exercise_list', views.exercise_list, name='exercise_list'),
    path('exercise/create/', views.exercise_new, name='exercise_new'),
    path('exercise/<int:pk>/edit/', views.exercise_edit, name='exercise_edit'),
    path('exercise/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
    path('activity_list', views.activity_list, name='activity_list'),
    path('activity/create/', views.activity_new, name='activity_new'),
    path('activity/<int:pk>/edit/', views.activity_edit, name='activity_edit'),
    path('activity/<int:pk>/delete/', views.activity_delete, name='activity_delete'),

]
