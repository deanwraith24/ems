from django.shortcuts import render

def landing_page(request):
    return render(request, 'users/landing.html')

def signup_page(request):
    return render(request, 'users/signup.html')