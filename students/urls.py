from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Export
    path('export/students/', views.export_students_excel, name='export_students'),
    path('export/results/', views.export_results_excel, name='export_results'),
    path('export/class/<str:class_name>/', views.export_class_report, name='export_class'),
    
    # Previous URLs
    path('', views.student_list, name='student_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.student_create, name='student_create'),
    path('<int:pk>/edit/', views.student_update, name='student_update'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('<int:pk>/result/', views.student_result, name='student_result'),
]