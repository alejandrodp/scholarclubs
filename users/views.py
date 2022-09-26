from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from .forms import StudentSignupForm, LoginForm, UpdateStudentProfileForm
from .models import StudentProfile


def home(request):
    return render(request, 'home.html')


class StudentSignupView(View):
    form_class = StudentSignupForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user: User = form.save()
            user.refresh_from_db()

            section = form.cleaned_data.get('section')
            StudentProfile.objects.update_or_create(user=user, section=section)
            user.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(StudentSignupView, self).dispatch(request, *args, **kwargs)


class UsersLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        return super(UsersLoginView, self).form_valid(form)


@login_required
def student_profile(request):
    if request.method == 'POST':
        profile_form = UpdateStudentProfileForm(request.POST, instance=request.user.studentprofile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        profile_form = UpdateStudentProfileForm(instance=request.user.studentprofile)

    return render(request, 'students/profile.html', {'profile_form': profile_form})

