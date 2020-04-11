from django.urls import path
from . import views
from django.conf.urls import url
# from mysite.core import views as core_views

urlpatterns = [
    path('', views.home, name='home'),
    path('artikel/', views.artikel, name='artikel'),
    path('signup/', views.signup, name="signup"),
]
