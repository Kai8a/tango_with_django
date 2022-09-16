from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('index/', views.index, name='inidex'),
    path('about/', views.about, name='about'),
]