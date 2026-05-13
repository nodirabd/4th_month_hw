import time
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import CustomRegistrationForm, LoginFormWithCaptcha
from .models import ResumeProfile

def get_simple_pseudo_code(digits=4):
    """Генерация 4-значного числа без random на основе микросекунд таймера"""
    timestamp = int(time.time() * 1000000)
    modulo = 10 ** digits
    code = timestamp % modulo
    return str(code).zfill(digits)

def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Создаем учетную запись пользователя
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginFormWithCaptcha(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # 2FA генерация кода 
                verification_code = get_simple_pseudo_code(4)
                
                # Записываем данные во временную сессию
                request.session['pre_auth_user_id'] = user.id
                request.session['auth_verification_code'] = verification_code
                
                # Отправка в консоль 
                send_mail(
                    'Код авторизации',
                    f'Ваш проверочный код: {verification_code}',
                    'hr@company.com',
                    [user.email],
                    fail_silently=False,
                )
                return redirect('verify_code')
            else:
                form.add_error(None, "Неверный логин или пароль")
    else:
        # Генерация чисел для примера капчи на базе времени
        seed = int(time.time() * 1000)
        n1 = (seed % 9) + 1  
        n2 = ((seed // 10) % 9) + 1
        form = LoginFormWithCaptcha(initial={'num1': n1, 'num2': n2})
    
    return render(request, 'users/login.html', {'form': form})

def verify_code_view(request):
    error = None
    if request.method == 'POST':
        user_code = request.POST.get('code')
        saved_code = request.session.get('auth_verification_code')
        user_id = request.session.get('pre_auth_user_id')
        
        if saved_code and user_code == saved_code:
            user = User.objects.get(id=user_id)
            login(request, user) # Авторизуем в системе
            
            # Очищаем сессию
            del request.session['auth_verification_code']
            del request.session['pre_auth_user_id']
            
            return redirect('dashboard')
        else:
            error = "Неверный код подтверждения!"
            
    return render(request, 'users/verify_code.html', {'error': error})

@login_required
def dashboard_view(request):
    # Показывает анкеты только авторизованным пользователям
    profiles = ResumeProfile.objects.all()
    return render(request, 'users/dashboard.html', {'profiles': profiles})
