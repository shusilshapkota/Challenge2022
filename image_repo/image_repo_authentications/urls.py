from django.urls import path
from .views import loginPage, registerPage

urlpatterns = [
    path('login/', loginPage.as_view(), name='login'),
    path('register/', registerPage.as_view(), name='register'),
]
