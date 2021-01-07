"""new_asmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from movies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('registration/', Registration.as_view()),
    # path('login/', Login.as_view()),
    path('add_poster/', AddPoster.as_view()),
    path('add_movie/', AddMovies.as_view()),
    path('update_movie/<int:pk>/', UpdateMovies.as_view()),
    path('delete_movie/<int:pk>/', DeleteMovies.as_view()),
    path('movie_list/', MoviesList.as_view()),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)