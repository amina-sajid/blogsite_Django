from django.urls import path
from bloggerz import views


urlpatterns = [

    path('index/', views.index),
    path('home/', views.home),
    path('', views.login),
    path('register/', views.register),

    path('userbase/', views.userbase),
    path('userreg/',views.userreg),
    path('post_details/',views.post_details),
    path('logout/',views.logout),
    path('comment/',views.comment),
    path('view_comments/', views.view_comments),
 ]
