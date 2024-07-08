
from django.contrib import admin
from django.urls import path
from medicoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('inner/', views.inner,name='inner'),
    path('about/', views.about,name='about'),
    path('doctor/', views.doctor,name='doctor'),
    path('departments/', views.departments,name='departments'),
    path('Contact/', views.contact,name='Contact'),

]
