from django import forms
from . models import Personalized,PersonalizedTour
from .widgets import DatePickerWidget, CounterTextInput, AutoCompleteSelect,LocationWidget, MultiDatePicker, BookingDatePickerWidget

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
                    'autocomplete': 'off',
                    'placeholder': 'only four numbers'
                }
            ),
            'Date': DatePickerWidget(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ex)18.09.02/18.09.02~18.09.20/18.09.20,18.09.25'
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
                    'autocomplete': 'off',
                    'placeholder': 'Ex) $20~$40'
                }
            ),
        }

class PersonalizedPostForm(forms.ModelForm):
    class Meta:
        model = PersonalizedTour
        fields = [
            'title',
            'Tourtype',
            'Country',
            'City',
            'Language',
            'BriefContent',
            'DetailContent',
            'HashTag',
            'MeetingPoint',
            'MeetingTime',
            'Map',
            'Direction',
            'Duration',
            'Price',
            'Minimum',
            'Maximum',
            'Price_include',
            'NotDate',
            'GuestInfo',
            'img',
            'SeasonFrom',
            'SeasonTo',
        ]
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Tourtype':forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                }
            ),
            'Country':AutoCompleteSelect(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control'
                }
            ),
            'City':forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control'
                }
            ),
            'Language':forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control'
                }
            ),
            'DetailContent':forms.Textarea(
                attrs={
                    'style': 'width:100%; height:240px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'placeholder': '당신이 만든 local 여행에 대한 설명을 자유롭게 작성해 주세요\n'
                    'Tip. 당신의 Tour만이 가지고 있는 특징에 대해 설명해 주세요.외국인은 언제나 local다움과 funny한 상품을 찾고있습니다.',
                    'class': 'form-control',
                    'id': 'detail'
                }
            ),
            'BriefContent':forms.Textarea(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'id': 'brief'
                }
            ),
            'HashTag':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'placeholder' : 'Ex) #Seoul #hiking #bicycle #picnic #localfood #picture #exercise #beer',
                    'autocomplete': 'off'
                }
            ),
            'MeetingPoint':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'placeholder': 'Ex) 94, Wausan-ro Mapo-gu Seoul',
                    'autocomplete': 'off'
                }
            ),
            'MeetingTime':forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                    'placeholder': 'Ex) 17:00'
                }
            ),
            'Map': LocationWidget(
                attrs={
                    'style': 'width:250px;'
                }

            ),
            'Direction':forms.Textarea(
                attrs={
                    'style': 'width:100%; height:130px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                }
            ),
            'Duration':forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                    'placeholder': 'Ex) 3hr 30min',
                    'autocomplete': 'off'
                }
            ),
            'Price':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Minimum' : forms.NumberInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Maximum': forms.NumberInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Price_include':forms.Textarea(
                attrs={
                    'style': 'width:100%; height:130px; margin-top:4px; border:1px solid gray;',
                    'placeholder' : 'Ex) traditional market, bicycle rental, Gyengbuk palace entree, dinner, lunch',
                    'class': 'form-control'
                }
            ),
            'NotDate': MultiDatePicker(
                attrs={
                    'style':'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'id': 'date',
                    'name': 'date',
                }
            ),
            'GuestInfo':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:130px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'img': forms.ClearableFileInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                    'multiple': True,
                }
            ),
            'SeasonFrom': DatePickerWidget(
                attrs={
                    'style':'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'SeasonTo': DatePickerWidget(
                attrs={
                    'style':'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'CourseName': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'DurationCourse': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'Photography': forms.ClearableFileInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'BriefCourse': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            )
        }

    def save(self, commit=True):
        post = PersonalizedTour(**self.cleaned_data)
        if commit:
            post.save()
        return post