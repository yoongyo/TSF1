from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Country, Language
from django.contrib.auth.forms import AuthenticationForm
from .widgets import AutoCompleteSelect

class SignupForm(UserCreationForm):
    pass

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')
    def clean_answer(self):
        if self.cleaned_data.get('answer', None) != 6:
            raise forms.ValidationError('땡~!!!')

class ProfileForm(forms.Form):
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    major = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    visitedCountry = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.Select(
            attrs={
                'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    nextCountry = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    interest = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'height:27px; margin-top:4px; border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    birth = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    emergency = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'

            }
        )

    )
    kakaoID = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    introduce = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'width:100%;height:108px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )
    gender = forms.CharField(
        widget=forms.Select(
            attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }
        )
    )

