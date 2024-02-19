from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('check_notes', views.check_notes, name='check_notes'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]