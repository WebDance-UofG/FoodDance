# FoodDance

# Overview
FoodDance, a web application where foodies, present and future food lovers can communicate witheach other, andshare their experiences on cooking.

On the one hand,FoodDanceprovides a free community environment for users to search and post their favorite recipes. Users can also comment and rate the recipes they have tried. On the other hand, the platform will recommend recipes to users according to their identity and on-demand, and users can add the recipes they want to try into their wish lists. The highest-rated recipes will be displayed to provide a reference for users.

In this project, we use sqlite 3 as database, use Django to implement the back-end service, and use html5, CSS, javascript, bootstrap 5 to process front-end render.

# Project Structure
└─ foodDance_web </br>
    ├─ fooddance </br>
    │  └─ templatetags </br>
    ├─ foodDance_web </br>
    ├─ media </br>
    │  ├─ avatars </br>
    │  └─ recipes </br>
    ├─ static </br>
    │  ├─ css </br>
    │  ├─ images </br>
    │  └─ js </br>
    └─ templates </br>
        └─ fooddance </br>


# Environment Requirement
This project uses python and django
 - Python 3.7.5
 - Django 2.1.5
 
**We recommend to use Anaconda Command Prompt.

    conda create -n fooddance python=3.7.5    
    conda activate fooddance

# Install
Open project, and run cmd, execute the following command:

    pip install -r requirements.txt
    cd foodDance_web

 Creating and migrating the database:

    python manage.py makemigrations fooddance
    python manage.py migrate

Import test data, run population script to do that, execute command:

    python population_script.py
Start up the server:

    python manage.py runserver

Project is disploy on the http://127.0.0.1:8000 (default port is 8000)

# Test
In fooddance_web file, run test command.

    python  manage.py test fooddance
   
# Web Page

## Index Page: /
 - [ ] **Today's Top** Show today's most views recipes.
 - [ ] **Recommendation** Show the top-9-comment recipes, click recipes can visit the detail of every recipe.
![index](https://user-images.githubusercontent.com/87979527/128576864-59744934-52f5-4800-8aa3-815c667b25d0.png)

## All Recipes Page: addrecipes/
 **Show all recipes**
![allrecipes](https://user-images.githubusercontent.com/87979527/128578990-127d7d9b-188b-41f6-bead-f84106d84a67.png)

## Search Result: search/?search=key
![search](https://user-images.githubusercontent.com/87979527/128579015-84c7693c-50b0-43b7-ba69-a63d7ef4142c.png)

## Login: login/
![login](https://user-images.githubusercontent.com/87979527/128579025-77f5e60a-8635-4e4e-affe-09f0425e5404.png)

## Sign Up: register/
![signup](https://user-images.githubusercontent.com/87979527/128580761-f28ade6b-c30f-474c-b067-12d4c0ce494e.png)

## My recipes: myrecipe/
Check my recipe
![myrecipes](https://user-images.githubusercontent.com/87979527/128580853-b4a1b040-b8db-4d6e-8629-11a6fa67827d.png)

# System Architecture
![未命名文件](https://user-images.githubusercontent.com/87979527/128576380-1edf78d9-b56a-4d64-a815-d3e97a6c7e37.png)

# Development Team

|                |name                          |email|
|----------------|-------------------------------|-----------------------------|
|1|Zumin Li            |2278100l@student.gla.ac.uk            |
|2          |Linyue Zhang           |2587334z@student.gla.ac.uk            |
|3          |Keyi Miao|2544119k@student.gla.ac.uk|
|4          |Qiaochu Xu|2544726X@student.gla.ac.uk|


