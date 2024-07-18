from django.urls import path
from . import views
from django.conf.urls.static import *

urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register_user"),
    path('home/', views.home, name="homePage"),
    path('about/', views.about, name='aboutPage'),
    path('contact/', views.contact, name='contactPage'),
    path('hotels/', views.hotels, name='hotelsPage'),
    path('flights/', views.flights, name='flightsPage'),
    path('citySearch/', views.citySearch, name='citySearchPage'),
    path('flightSearch/', views.flight_search, name='flightSearchPage'),
    path('hotelDetails/<slug>/', views.detailHotel, name="detailHotelPage"),
]