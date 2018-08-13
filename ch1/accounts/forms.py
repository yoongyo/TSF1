from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


from .models import Profile, Country, Language
from django.contrib.auth.forms import AuthenticationForm
import unicodedata
from django.core.validators import validate_email
from .models import Profile
from .widgets import DatePickerWidget, ProfileWidget
from django_select2.forms import ModelSelect2MultipleWidget

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = '이메일 형식으로 입력 가능합니다.'
        self.fields['username'].label = '이메일'
        self.fields['username'].widget = forms.EmailInput(
            attrs={'class':'form-control','style':'margin-top:30px;margin-bottom:14px;','placeholder':'Your Email','autocomplete': 'off'}

        )
        #self.fields['password1'].validators = password_validation.password_validators_help_text_html(),
        self.fields['password1'].help_text = '비밀번호 형식에 맞게 넣어주세요'
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control','style':'margin-bottom:14px;', 'placeholder':'Password','autocomplete': 'off'}
        )
        self.fields['password2'].validators = []
        self.fields['password2'].help_text = "Enter the same password as before, for verification."
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control','style':'margin-bottom:20px;', 'placeholder':'Confirm Password', 'autocomplete': 'off'}
        )

    error_messages = {
        'password_mismatch': "The two password fields didn't match."
    }
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


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
            'name',
            'img',
            'video'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'language' : forms.Select(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control'
            }),
            'major': forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control',
                'autocomplete': 'off'
            }),
            'visitedCountry': ModelSelect2MultipleWidget(
                model=Country,
                search_fields=['name__icontains'],
                attrs = {
                    'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
                    'class':'form-control js-example-basic-multiple',
                    'multiple': 'multiple',
                }
            ),
            'nextCountry': ModelSelect2MultipleWidget(
                model=Country,
                search_fields=['name__icontains'],
                attrs = {
                    'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
                    'class':'form-control js-example-basic-multiple',
                    'multiple': 'multiple',
                }
            ),
            'interest': forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px; border: 1px solid gray;',
                'class': 'form-control',
                'placeholder': '예시: #soccer #photo #travel #cook #activity',
                'autocomplete': 'off'
            }),
            'birth': DatePickerWidget(attrs={
                'style':'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'email':forms.EmailInput(attrs={
                'style':  'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control',
                'autocomplete': 'off'
            }),
            'emergency':forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control',
                'autocomplete': 'off',
                'placeholder': '- 없이 숫자만 입력',
            }),
            'kakaoID':forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control',
                'autocomplete': 'off'
            }),
            'introduce':forms.Textarea(attrs={
                'style': 'width:100%;height:160px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control',
                'autocomplete': 'off'
            }),
            'phone_number':forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control',
                'placeholder': '- 없이 숫자만 입력',
                'autocomplete': 'off'
            }),
            'gender': forms.Select(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class': 'form-control',
            }),
            'img': ProfileWidget(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class':'form-control',
                'name': 'input-file-preview',
            }),
            'video': forms.TextInput(attrs={
                'style': 'height:27px; margin-top:4px;border: 1px solid gray;',
                'class': 'form-control',
            }),

        }
