from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyse/', views.analyse, name='analyse'),
    path('signup/', views.signup, name='signup'),
    path('history/', views.history, name='history'),
    path('delete/<int:pk>/', views.delete_result, name='delete_result'),
    path('download/<int:pk>/', views.download_result, name='download_result'),
]