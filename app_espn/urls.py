from django.urls import path
from . import views
from django.conf.urls import url
# from mysite.core import views as core_views

urlpatterns = [
    path('', views.home, name='home'),
    path('artikel', views.artikel, name='artikel'),
    path('football', views.football, name="football"),
    path('nba', views.nba, name="nba"),
    path('nfl', views.nfl, name="nfl"),
    path('cricket', views.cricket, name="cricket"),
    path('rugby', views.rugby, name="rugby"),
    path('golf', views.golf, name="golf")
    

]
