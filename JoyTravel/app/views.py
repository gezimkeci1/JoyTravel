from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hotels(request):
    return render(request, 'hotels.html')

def flights(request):
    return render(request, 'flights.html')

def detailHotel(request, slug):
    hotelDetail = Hotel.objects.get(slug=slug)
    context = {"hotelDetail":hotelDetail}
    return render(request, 'hotelDetails.html', context)
    
def citySearch(request):
    if request.method == "POST":
        city = request.POST.get('citySearch', '').strip()
        checkin = request.POST.get('checkin', '').strip()
        checkout = request.POST.get('checkout', '').strip()
        adults = request.POST.get('adults', '').strip()
        children = request.POST.get('children', '').strip()

        city_search_term = request.POST['citySearch']
        cities = City.objects.filter(name__icontains=city_search_term)
        hotels = Hotel.objects.filter(city__in=cities) if cities.exists() else []
        context = {
            'citySearch': city_search_term,
            'cities': cities,
            'hotels': hotels,
        }

        if city != '' and checkin != '' and checkout != '' and adults != '' and children != '' and cities.exists():
            return render(request, 'citySearch.html', context)
        else:
            messages.error(request, 'There is no hotels in the city you searched for or you need to fill in all the fields!')
    return render(request, 'hotels.html', context)

def flight_search(request):
    if request.method == "POST":
        city_name = request.POST.get('citySearch', '').strip()
        departure_date = request.POST.get('departure', '').strip()
        return_date = request.POST.get('return', '').strip()
        seats = request.POST.get('seats', '').strip()

        city_search_term = request.POST.get('citySearch', '')
        cities = City.objects.filter(name__icontains=city_search_term)
        flights = Flight.objects.filter(city__in=cities) if cities.exists() else []

        context = {
            'citySearch': city_search_term,
            'cities': cities,
            'flights': flights,
        }

        if city_name and departure_date and return_date and seats and cities.exists():
            return render(request, 'flightSearch.html', context)
        else:
            messages.error(request, 'No flights available for your search criteria or you need to fill in all the fields!')
    
    return render(request, 'flights.html', context)

def contact(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName', '').strip()
        lastName = request.POST.get('lastName', '').strip()
        email = request.POST.get('email', '').strip()
        contactMessage = request.POST.get('contactMessage', '').strip()

        if firstName and lastName and email and contactMessage:
            Contact.objects.create(
                contactName=firstName,
                contactLastName=lastName,
                contactEmail=email,
                contactMessage=contactMessage
            )
            messages.success(request, 'Your message has been sent! You will be contacted by our team shortly.')
        else:
            messages.error(request, 'Please fill all the fields!')
    context = {}
    return render(request, 'contact.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control form-control-lg input'

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homePage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register_user.html', {'form':form})