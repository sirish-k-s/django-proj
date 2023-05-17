from django.urls import path
from basicApp import views

app_name = 'basicApp'

urlpatterns = [
    path('register/', views.registeration, name="register"),
    path('login/', views.user_login_view, name='login'),
]