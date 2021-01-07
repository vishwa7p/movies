# movies_app 

# Overview
This application helps the user to add, update, and delete movies and add posters of the movies, here django and djangorestframework is used for the server side of the application.

Please follow the setup instrutions as follow in order to view the complete app we need to setup our backend so be carefull otherwise there could be problems.

# Backend-Setup 

clone the repositroy:-
```
https://github.com/vishwa7p/movies.git
```
Create Virtual env:-
```
virtualenv app
```
Activate Virtual env:-
```
```
Install Dependencies:-
```
pip3 install -r requirements.txt
```
In Settings.py file should add the database credentials like below,
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '*****',
        'USER': '******',
        'PASSWORD': '******',
        'HOST': 'localhost',
    }
}
```
Make Migrations:-
```
./manage.py makemigrations
./manage.py migrate
```
Start server for your REST-API:-
```
./manage.py runserver
```
So apparently to server is running localhost:8000(django-api).....
