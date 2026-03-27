from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.Home ,name='Home'),
    path('education/',views.Education, name='education'),
    path('projects/' ,views.Projects , name='projects'),
    path('extras/', views.Extras, name='extra'),
    path('extras/travel/', views.travel, name='travel'),
    path('contact/', views.contact, name='contact'),
    path('education/certificates', views.Certificates, name='certificate')

]
