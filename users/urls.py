from django.urls import path

from .views import home, StudentSignupView, student_profile, admin_statistics

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', StudentSignupView.as_view(), name='users-register'),
    path('profile/', student_profile, name='users-profile'),
    path('statistics/', admin_statistics, name='admin'),
]
