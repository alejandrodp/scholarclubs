from django.urls import path
from .views import home, StudentSignupView, student_profile

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', StudentSignupView.as_view(), name='users-register'),
    path('profile/', student_profile, name='users-profile'),
]
