# FoodDance

# Overview
FoodDance, a web application where foodies, present and future food lovers can communicate witheach other, andshare their experiences on cooking.

On the one hand,FoodDanceprovides a free community environment for users to search and post their favorite recipes. Users can also comment and rate the recipes they have tried. On the other hand, the platform will recommend recipes to users according to their identity and on-demand, and users can add the recipes they want to try into their wish lists. The highest-rated recipes will be displayed to provide a reference for users.

In this project, we use sqlite 3 as database, use Django to implement the back-end service, and use html5, CSS, javascript, bootstrap 5 to process front-end render.

# Environment Requirement
This project uses python and django
 - Python 3.7.5
 - Django 2.1.5
 
We recommend to use Anaconda Command Prompt.

    conda create -n fooddance python=3.7.5    
    conda activate fooddance
    conda install django==2.1.5
    conda install pillow
# Install
 **Enter file: FoodDance/FoodDanceWeb, open cmd.**

 

**Load virtual environment:**

    conda activate fooddance

 
 **Creating and migrating the Database:**
   

     python manage.py migrate

  **Start up the project:**
   

    python manage.py runserver

**Project is disploy on the http://127.0.0.1:8000** (default port is 8000)
# Demo
if you want to use demo, run population script to Import test data

    python populate.py

and then run:

    python manage.py runserver
# Development Team

|                |name                          |email|
|----------------|-------------------------------|-----------------------------|
|1|Zumin Li            |2278100l@student.gla.ac.uk            |
|2          |Linyue Zhang           |2587334z@student.gla.ac.uk            |
|3          |Keyi Miao|2544119k@student.gla.ac.uk|
|4          |Qiaochu Xu|2544726X@student.gla.ac.uk|


# System Architecture
![未命名文件](https://user-images.githubusercontent.com/87979527/128576380-1edf78d9-b56a-4d64-a815-d3e97a6c7e37.png)

