from django.urls import path
from memorial import views

app_name = 'memorial'
urlpatterns= [
    path('', views.home, name='home')
]