from django.contrib import admin

from django.contrib.auth import views as auth_views

from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.index,name='home'),
    path('customer/<str:pk_test>/', views.customer,name='customer'),
    path('products/', views.products,name='products'),
    path('create_order/<str:pk>/', views.CreateOrder,name='create_order'),
    path('update_order/<str:pk>/', views.UpdateOrder,name='update_order'),
    path('delete_order/<str:pk>/', views.DeleteOrder,name='delete_order'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('user/',views.userPage,name='user-page'),
    path('account/',views.accountSettings,name='account'),
     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>[0-9A-Za-z]+)-<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

]