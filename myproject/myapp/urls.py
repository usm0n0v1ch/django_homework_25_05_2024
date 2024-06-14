from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('switch/<int:task_id>/', views.task_switch, name='task_switch'),
]