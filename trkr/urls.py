from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from django.urls import path, re_path

app_name = 'trkr'
urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
    path('', TemplateView.as_view(template_name="trkr/home.html"), name='home'),
    path('client_list', views.client_list, name='client_list'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),
    # path('match_list', views.match_list, name='match_list'),
    # path('match/<int:pk>/edit/', views.match_edit, name='match_edit'),
    # path('team_list', views.team_list, name='team_list'),
    # path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    # path('player_list', views.player_list, name='player_list'),
    # path('player/<int:pk>/edit/', views.player_edit, name='player_edit'),
    # path('player/<int:pk>/delete/', views.player_delete, name='player_delete'),
    # path('player/create/', views.player_new, name='player_new'),

]
