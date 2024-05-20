from django.urls import path
from userauth import views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('sign_in/home', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('index', views.index, name='index'),
    path('home/', views.home, name='home'),
    # #path('activate/<uidb64>/<token>', views.activate, name='account_activation'),
]