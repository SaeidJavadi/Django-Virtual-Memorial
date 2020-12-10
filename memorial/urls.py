from django.urls import path
from memorial import views

app_name = 'memorial'
urlpatterns= [
    path('', views.home, name='home'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('add1', views.DeveasedCreate.as_view(), name='add_Deveased'),
    path('list', views.list, name='list_Deveased'),
]