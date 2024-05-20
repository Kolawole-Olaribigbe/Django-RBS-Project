from django.urls import path
from hotel import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    

]