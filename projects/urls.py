from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ProjectView.as_view(), name='project'),
]
