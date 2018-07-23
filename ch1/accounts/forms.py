from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import extras

from .models import Profile, Country, Language
from django.contrib.auth.forms import AuthenticationForm
from .widgets import AutoCompleteSelect
import unicodedata
from django.core.validators import validate_email
from .models import Profile
from .widgets import AutoCompleteSelect

class SignupForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = '이메일 형식으로 입력 가능합니다.'
        self.fields['username'].label = '이메일'
        self.fields['username'].widget = forms.EmailInput(
            attrs={'class':'form-control'}
        )
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control'}
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control'}
        )


    def save(self, commit=True):
        user = super().save()
        user.email = user.username

        if commit:
            user.save()
        return user

    """
    def clean_username(self):
        value = self.cleaned_data('username')
        if value:
            validate_email(value)
        return value
    """

class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label= 'Email',
        widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control', 'placeholder':'Your Email', 'requidred':True, 'style':'margin-top:20px; margin-bottom: 10px;'})
    )
    password = forms.CharField(
        label= "Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'upw', 'placeholder':'Password', 'required': True}),
    )

class ProfileMForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {
            'language',
            'major',
            'visitedCountry',
            'nextCountry',
            'interest',
            'birth',
            'email',
            'emergency',
            'kakaoID',
            'phone_number',
            'introduce',
            'gender',
        }
        widgets = {
            'language' : forms.Select(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'major': forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'visitedCountry':AutoCompleteSelect(attrs={
                'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'nextCountry':AutoCompleteSelect(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'interest': forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px; border: 1px solid gray;',
                'class':'form-control'
            }),
            'birth':extras.SelectDateWidget(attrs={
                'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
            }),
            'email':forms.EmailInput(attrs={
                'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'emergency':forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'kakaoID':forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'introduce':forms.Textarea(attrs={
                'style': 'width:100%;height:108px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'phone_number':forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'gender':forms.Select(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
        }

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
        widget=extras.SelectDateWidget(
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

