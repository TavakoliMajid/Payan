from django.http import HttpResponse
from django.shortcuts import render
def home (request):
    return render(request, 'VintedProject/home.html')

def contact(request):
    return render(request, 'VintedProject/contact.html')

def signup(request):
    return render(request, 'VintedProject/signup.html')

def sell (request):
    return  render(request, "VintedProject/sell.html")

def buy(request):
    return render(request, 'VintedProject/buy.html')

