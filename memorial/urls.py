from django.urls import path
from memorial import views

app_name = 'memorial'
urlpatterns= [
    path('', views.home, name='home'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('add1', views.DeveasedCreate.as_view(), name='add_Deveased'),
    path('edit/<int:id>/', views.DeveasedEdit, name='edit_Deveased'),
    path('list', views.list, name='list_Deveased'),
    path('delete/<int:id>/', views.delete, name='del_Deveased'),
    # path('<int:pk>/', views.DeadDetailView.as_view(), name='view_Deveased'),
    path('<int:pk>/', views.DeadView, name='view_Deveased'),
]