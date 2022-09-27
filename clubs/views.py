from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from clubs.forms import ClubSuggestForm, ClubSelectionForm
from clubs.models import Club


@login_required
def new_club(request):
    if request.method == 'POST':
        club_form = ClubSuggestForm(request.POST)

        if club_form.is_valid():
            user = request.user
            club_form.instance.student = user
            club_name = club_form.cleaned_data['name']

            if Club.objects.filter(name=club_name).exists():
                club = Club.objects.get(name=club_name)
                messages.success(request, 'Club already exists, added to clubs of interest')
                if not club.studentprofile_set.filter(user=request.user).exists():
                    user.studentprofile.interested_clubs.add(club)
            else:
                club = club_form.save()
                messages.success(request, 'Your club was saved successfully')
                user.studentprofile.interested_clubs.add(club)

            return redirect(to='/')

    else:
        club_form = ClubSuggestForm()

    return render(request, 'new_club.html', {'form': club_form})


@login_required
def select_clubs(request):
    user = request.user
    if request.method == 'POST':
        club_form = ClubSelectionForm(request.POST)

        if club_form.is_valid():
            clubs = club_form.cleaned_data['clubs']

            user.studentprofile.interested_clubs.set(clubs)

            user.studentprofile.save()

            return redirect(to='/')

    else:
        club_form = ClubSelectionForm(initial={'clubs': user.studentprofile.interested_clubs.all()})

    return render(request, 'select_club.html', {'form': club_form})
