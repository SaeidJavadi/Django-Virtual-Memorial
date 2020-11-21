from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/',views.LoginPage, name='login'),
    path('register/',views.RegisterPage, name='register'),
    path('verify/',views.VerifyPage, name='verify'),
]