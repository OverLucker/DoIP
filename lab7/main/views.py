from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .forms import RegistrationForm, AuthorizationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# view to display registration form
class RegistrationView(View):
    def get(self, request):
        return render(
            request,
            'registration.html',
            context={
                'page': {'title': 'Registration page'},
                'form': RegistrationForm(),
            }
        )

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth')

        # return JsonResponse(form.errors)
        return render(
            request,
            'registration.html',
            context={
                'page': {'title': 'Registration page'},
                'form': form,
            }
        )


class AuthorizationView(View):
    def get(self, request):
        return render(
            request,
            'authorization.html',
            context={
                'page': {'title': 'Authorization page'},
                'form': AuthorizationForm(),
            }
        )

    def post(self, request):
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('index')

        return render(
            request,
            'authorization.html',
            context={
                'page': {'title': 'Authorization page'},
                'form': form,
            }
        )


@login_required(login_url='auth')
def index(request):
    return render(
            request,
            'index.html',
            context={
                'page': {'title': 'Success'},
            }
        )
