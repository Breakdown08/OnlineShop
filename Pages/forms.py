from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from .models import New


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Псевдоним пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name')
        help_texts = {
            'username': None
        }

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned_data['password2']


class CreateNewForm(forms.ModelForm):
    class Meta:
        model = New
        exclude = ('author', 'slug', 'created_at')
        widgets = {
            'title': forms.TextInput(attrs={'value': '',
                                            'type': 'text',
                                            'class': 'form-control',
                                            'placeholder': 'Заголовок',
                                            'id': 'title'}),
            'short_description': forms.Textarea(attrs={'value': '',
                                                       'type': 'text',
                                                       'class': 'form-control',
                                                       'placeholder': 'Краткое описание',
                                                       'id': 'short_description'}),
            'content': forms.CharField(widget=CKEditorWidget()),
        }