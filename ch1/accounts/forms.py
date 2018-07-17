from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Country, Language
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    def save(self):
        user = super().save()
        profile = Profile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user

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
                'style': 'width:100%; hegith:30px; margin-top:4px;'
            }
        )
    )
    major = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    visitedCountry = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    nextCountry = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    interest = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.ClearableFileInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    emergency = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )

    )
    kakaoID = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    introduce = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'width:100%; height:130px; margin-top:4px;'
            }
        )
    )

