from django.urls import path
from .views import loginPage, registerPage, logoutUser

urlpatterns = [
    path('login/', loginPage.as_view(), name='login'),
    path('register/', registerPage.as_view(), name='register'),
    path('logout/', logoutUser.as_view(), name='logout'),
]
