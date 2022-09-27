from django.urls import path

from clubs.views import new_club, select_clubs

urlpatterns = [
    path('', new_club, name='new-club'),
    path('interest/', select_clubs, name='select-clubs')
]
