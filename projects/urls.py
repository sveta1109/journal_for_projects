from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path('', views.project_list, name="project_list"),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('c/<int:pk>/', views.chapter_detail, name="chapter_detail"),
    path('task/<int:pk>/toggle/', views.toggle_task, name="toggle_task"),
]