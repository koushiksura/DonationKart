from django.urls import path,include, re_path
from . import views

app_name = 'login'

urlpatterns = [
    re_path('^$', views.home, name="login.home"),
    path('accounts/', views.login, name="login.login"),
    path('profile/', views.view_profile, name='login.view_profile'),

]
