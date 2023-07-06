from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('welcome/', views.previously_created_1, name='welcome'),
]
