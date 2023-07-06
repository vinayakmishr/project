from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
            path('',views.frontpage, name='frontpage'),
            path('sinup/',views.sinup, name='sinup'),
            path('login/',auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
            path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]