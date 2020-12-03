from django.contrib import admin
from django.urls import path,include
from. import views


urlpatterns = [
    path('', views.homeview, name="home"),
    path('home/', views.homeview, name="main"),
    path('courses/', views.courses, name="courses"),
    path('audioediting/', views.audioediting, name="audioediting"),
    path('videoediting/', views.vide, name="videoediting"),
    path('about/', views.about, name="about"),
    path('direction/', views.direct, name="direction"),
    path('cinematography/', views.camee, name="cinematography"),
    path('pricing/', views.pricing, name="pricing"),
    path('trainers/', views.trainers, name="trainers"),
    path('costum/', views.costum, name="costum"),
    path('costum/upload/', views.resumeupload, name="costum"),
    path('audioequipment/', views.audi, name="audio equipment"),
    path('hired/', views.hired, name="hired"),
    path('movieinfo/', views.moviee, name="movieinfo"),
    path('screenw/', views.sws, name="screenw"),
    path('signup/', views.loginn, name="signup"),
    path('login/', views.loginnn, name="login"),
    path('logout/', views.LogoutUser, name="logout"),

]
