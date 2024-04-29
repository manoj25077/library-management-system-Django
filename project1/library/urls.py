from django.contrib import admin
from django.urls import path
from library import views as app_view
from django.conf.urls.static import static
from project1 import settings
urlpatterns = [
    path('',app_view.home,name = 'home'),
    path('usersignup',app_view.usersignup,name='usersignup'),
    path('adminsignup',app_view.adminsignup,name='adminsignup'),
    path('userlogin',app_view.userlogin,name='userlogin'),
    path('adminlogin',app_view.adminlogin,name='adminlogin'),
    path('bookdetails',app_view.bookdetails,name='Bookdetails'),
    path('take',app_view.take,name='take'),
    path('takebook/<pk>',app_view.takebook,name='takebook'),
    path('retainbook/<pk>',app_view.retainbook,name='retainbook'),
    path('add_book',app_view.lib,name='book'),
    path('updatebook/<pk>',app_view.updatebook,name='updatebook'),
    path('deletebook/<pk>',app_view.deletebook,name='deletebook'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
