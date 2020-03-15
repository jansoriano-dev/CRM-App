from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
        path('logout/',views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="useraccount"),

    path('account/', views.accountSettings, name="account"),


    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('createorder/<str:pk>/', views.createOrder, name="createorder"),
    path('updateorder/<str:pk>/', views.updateOrder, name="updateorder"),
    path('deleteorder/<str:pk>/', views.deleteOrder, name="deleteorder"),

    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name = "accounts/passwordReset.html"),name='reset_password'),
    path('resetpasswordsent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/passwordResetSent.html"),name='password_reset_done'),    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/passwordResetForm.html"), name='password_reset_confirm'),
    path('resetpasswordcomplete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/passwordResetDone.html"), name='password_reset_complete'),

]
