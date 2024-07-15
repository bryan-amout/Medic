
from django.contrib import admin
from django.urls import path
from medicoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('doctor/', views.doctor, name='doctor'),
    path('departments/', views.departments, name='departments'),
    path('Contact/', views.contact, name='Contact'),
    path('Application/', views.Application, name='application'),
    path('show/', views.show, name='show'),
    path('appointment/', views.application, name='appoint'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),



]
