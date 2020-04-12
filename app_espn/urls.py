from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('artikel/', views.artikel, name='artikel'),
    path('signup/', views.signup, name="signup"),
    path('search/', views.search, name="search"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('artikel/<int:artikel_id>/', views.artikel_detail, name='artikel_detail'),
    path('artikel/clap/<int:artikel_id>/',views.artikel_detail_add_like),
    path('football', views.football, name="football"),
    path('nba', views.nba, name="nba"),
    path('nfl', views.nfl, name="nfl"),
    path('cricket', views.cricket, name="cricket"),
    path('rugby', views.rugby, name="rugby"),
    path('golf', views.golf, name="golf")
]


