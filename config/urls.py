from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/login/')

urlpatterns = [
    path('', include('analyser.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='analyser/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]