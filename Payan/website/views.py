from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import json


# Render pages
def home(request):
    return render(request, 'index.html')


def buy(request):
    return render(request, 'buy.html')


def sell(request):
    return render(request, 'sell.html')


def login_view(request):
    return render(request, 'login.html')


def signup_page(request):  # Renamed to avoid conflict
    return render(request, 'signup.html')


# API: Check if email exists
def check_email(request):
    email = request.GET.get("email")
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({"exists": exists})


# API: Login user
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        user = User.objects.filter(email=email).first()

        if user:
            login(request, user)
            return JsonResponse({"success": True, "username": user.first_name})

    return JsonResponse({"success": False})


# API: Guest Login
def guest_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session["guest_name"] = data.get("name")
        return JsonResponse({"success": True, "name": data.get("name")})


# API: Sign Up User
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        name = data.get("name")
        lastname = data.get("lastname")
        phone = data.get("phone")

        # Create user with a temporary password (should be changed later)
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=name,
            last_name=lastname,
            password="temporarypassword"  # Change this later!
        )

        login(request, user)  # Auto-login after sign-up
        return JsonResponse({"success": True, "username": name})

    return JsonResponse({"success": False})
