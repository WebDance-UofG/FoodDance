from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.urls import reverse


app_name = 'fooddance'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:recipe_title_slug>/', views.detail, name="detail"),
    path('detail/<slug:recipe_title_slug>/*', views.detail),
    path('login/', views.user_login, name="user_login"),
    path('register/', views.user_register, name="user_register"),
    path('allrecipes/', views.category_allrecipes, name="all_recipes"),
    path('search/', views.search, name="search"),
    path('logout/', views.user_logout, name="logout"),
    path('like/', views.like, name="like"),
    path('collect/', views.collect, name="collect"),
    path('share/', views.share, name="share"),

]
