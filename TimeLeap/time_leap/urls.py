from django.conf.urls import url
from django.urls import path
from time_leap import views

urlpatterns = [
    path('', views.index, name='index'),
]
