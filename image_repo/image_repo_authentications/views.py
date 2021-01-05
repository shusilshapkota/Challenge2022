from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import CreateUserForm
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# This page handles user logins and redirect to sign up if necessary
class loginPage(APIView):
    def get(self, request):
        context = {}
        return render(request, 'auth/login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response("User Logged In", status=status.HTTP_200_OK)
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')


# This page handles user sign ups and redirects to log in page after signing up
class registerPage(APIView):
    def get(self, request):
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'auth/register.html', context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
        return redirect('login')
