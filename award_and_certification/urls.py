from django.urls import path
from . import views

urlpatterns = [
    path('', views.award_list, name='award_list'),
] 