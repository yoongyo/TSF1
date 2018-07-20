from django import forms
from .models import Language,Nationality,SNS,Booking
from .widgets import DatePickerWidget, CounterTextInput


class BookMForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'LastName':forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'FirstName':forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Age':forms.NumberInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'

                }
            ),
            'Gender':forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Email':forms.EmailInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Date': DatePickerWidget(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'SNS':forms.Select(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Nationality':forms.Select(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'phone':forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'ConfirmedEmail':forms.EmailInput(
                attrs={
                    'style':'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Language':forms.Select(
                attrs={
                    'style': 'border:1px solid gray; height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'SNSID':forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Demand': CounterTextInput(
                attrs={
                    'style': 'width:100%; height:130px; border:1px solid gray;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
        }

class BookForm(forms.Form):
    LastName = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    FirstName = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    Age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'

            }
        )
    )
    Gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    Date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
            }
        )
    )
    SNS = forms.ModelChoiceField(
        queryset=SNS.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    Nationality = forms.ModelChoiceField(
        queryset=Nationality.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    ConfirmedEmail = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'style':'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    Language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'border:1px solid gray; height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    SNSID = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )
    Demand = forms.CharField(
        max_length=1200,
        widget=forms.Textarea(
            attrs={
                'style': 'width:100%; height:130px; border:1px solid gray;margin-top:3px;',
                'class': 'form-control'
            }
        )
    )