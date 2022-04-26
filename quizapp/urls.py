import imp
from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.adminlogin, name="adminlogin"),
    path('Index/', views.Index, name="Index"),
    path('index/', views.adminLoginpost, name="adminLoginpost"),
    path('adminIndex/', views.adminIndex, name="adminIndex"),

    path('createQuestions/', views.createQuestions, name="createQuestions"),
    path('saveQuestions/', views.saveQuestions, name="saveQuestions"),
    path('showAllQuestion/', views.showAllQuestion, name="showAllQuestion"),
    path('editques/<int:note_id>', views.editques, name="editques"),
    path('updateques/', views.updateques, name="updateques"),
    path('deleteques/<int:note_id>', views.deleteques, name="deleteques"),

    path('adminLogout/', views.adminLogout, name="adminLogout"),


    path('register', views.register, name="register"),
    path('userRegister', views.userRegister, name="userRegister"),
    path('userLoginForm', views.userLoginForm, name="userLoginForm"),
    path('userLogin', views.userLogin, name="userLogin"),


    path('startQuiz', views.startQuiz, name="startQuiz"),
    path('userProfile', views.userProfile, name="userProfile"),
    path('userLogout', views.userLogout, name="userLogout"),

    path('sendEmail', views.sendEmail, name="sendEmail"),
    
   
]
urlpatterns += staticfiles_urlpatterns()