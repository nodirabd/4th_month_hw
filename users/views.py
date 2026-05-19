import time
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models, forms
from .models import ResumeProfile

def get_simple_pseudo_code(digits=4):
    timestamp = int(time.time() * 1000000)
    modulo = 10 ** digits
    code = timestamp % modulo
    return str(code).zfill(digits)

class RegisterView(generic.View):
    def get(self, request):
        form = forms.CustomRegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = forms.CustomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
        return render(request, 'users/register.html', {'form': form})

class LoginView(generic.View):
    def get(self, request):
        seed = int(time.time() * 1000)
        n1 = (seed % 9) + 1
        n2 = ((seed // 10) % 9) + 1
        form = forms.LoginFormWithCaptcha(initial={'num1': n1, 'num2': n2})
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginFormWithCaptcha(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                verification_code = get_simple_pseudo_code(4)
                request.session['pre_auth_user_id'] = user.id
                request.session['auth_verification_code'] = verification_code
                return redirect('verify_code')
            else:
                form.add_error(None, "Неверный логин или пароль")
        return render(request, 'users/login.html', {'form': form})

class VerifyCodeView(generic.View):
    def get(self, request):
        return render(request, 'users/verify_code.html', {'error': None})

    def post(self, request):
        error = None
        user_code = request.POST.get('code')
        saved_code = request.session.get('auth_verification_code')
        user_id = request.session.get('pre_auth_user_id')

        if saved_code and user_code == saved_code:
            user = User.objects.get(id=user_id)
            login(request, user)
            
            del request.session['auth_verification_code']
            del request.session['pre_auth_user_id']
            
            return redirect('dashboard')
        else:
            error = "Неверный код подтверждения!"
        
        return render(request, 'users/verify_code.html', {'error': error})

@method_decorator(login_required, name='dispatch')
class DashboardView(generic.View):
    def get(self, request):
        profiles = ResumeProfile.objects.all()
        return render(request, 'users/dashboard.html', {'profiles': profiles})