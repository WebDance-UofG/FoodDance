from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:recipe_title_slug>', views.detail, name="detail")
]
