from django.urls import path
from . import views

app_name = 'langrec'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('htmx/recommend/', views.recommend, name='recommend'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
