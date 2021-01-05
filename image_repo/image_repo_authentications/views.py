from django.shortcuts import render
from rest_framework.views import APIView
from .forms import CreateUserForm

# Create your views here.

# This page handles user logins and redirect to sign up if necessary
class loginPage(APIView):
    def get(self, request):
        context = {}
        return render(request, 'auth/login.html', context)

class registerPage(APIView):
    def get(self, request):
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'auth/register.html', context)
