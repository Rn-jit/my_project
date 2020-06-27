from todoapp import views
from django.urls import path

app_name = 'todoapp'

urlpatterns = [
    path('todoapp/', views.todoapp, name='todoapp'),
    path('delete/<pk>/', views.delete, name='delete'),
    path('edit/<pk>', views.edit_list, name='edit_list'),
]