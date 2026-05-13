from django import forms
from django.contrib.auth.models import User
from .models import ResumeProfile

class CustomRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Логин")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")

    class Meta:
        model = ResumeProfile
        fields = [
            'full_name', 'birth_date', 'phone', 'city', 
            'education', 'experience_years', 'desired_salary', 
            'skills', 'photo', 'resume_file'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'skills': forms.Textarea(attrs={'rows': 3}),
        }

class LoginFormWithCaptcha(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
    
    # Скрытые поля для валидации капчи без сессий на этапе генерации формы
    num1 = forms.IntegerField(widget=forms.HiddenInput())
    num2 = forms.IntegerField(widget=forms.HiddenInput())
    captcha_input = forms.IntegerField(label="Решите пример")

    def clean(self):
        cleaned_data = super().clean()
        n1 = cleaned_data.get('num1')
        n2 = cleaned_data.get('num2')
        user_ans = cleaned_data.get('captcha_input')
        
        if n1 is not None and n2 is not None and user_ans is not None:
            if n1 + n2 != user_ans:
                raise forms.ValidationError("Неверный ответ капчи! Вы робот?")
        return cleaned_data
