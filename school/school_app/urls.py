from django.urls import path
from . import views

app_name = 'school'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('ajax/load-course/', views.load_course, name='ajax_load_course'),
]
