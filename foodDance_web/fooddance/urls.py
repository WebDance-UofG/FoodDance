from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = 'fooddance'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:recipe_title_slug>/', views.detail, name="detail"),
    path('login/', views.login, name="login"),
    path('allrecipes/', views.category_allrecipes, name="all_recipes"),
    path('search/', views.search, name="search")

]
