
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_employee, name='register_employee'),
    path('list/', views.employee_list, name='employee_list'),

    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('performance/', views.employee_performance, name='employee_performance'),
]
