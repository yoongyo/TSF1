from django import forms
from . models import Personalized
from . widgets import DatePickerWidget

class PersonalizedForm(forms.ModelForm):
    class Meta:
        model = Personalized
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'FirstName':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'LastName': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Gender': forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'City': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Email': forms.EmailInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Password': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Date': DatePickerWidget(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'SNS': forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Nationality': forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Language': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Cellnumber': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'SNSID': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Content': forms.Textarea(
                attrs={
                    'style': 'width:100%; height:130px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Guest': forms.NumberInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Price': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
        }