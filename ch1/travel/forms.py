from .models import Post, Country, TypeOfTour, City, Language, SNS, Booking
from django import forms
from .widgets import DatePickerWidget, CounterTextInput, AutoCompleteSelect,LocationWidget

from django.core.urlresolvers import reverse_lazy
import sys
sys.path.append('..')
from mysite.widgets.naver_map_point_widget import NaverMapPointWidget



class PostMForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'Tourtype',
            'Country',
            'City',
            'Language',
            'DetailContent',
            'BriefContent',
            'HashTag',
            'MeetingPoint',
            'MeetingTime',
            'Map',
            'Direction',
            'CourseName',
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
            'CourseName',
            'DurationCourse',
            'Photography',
            'BriefCourse',
        ]
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control'
                }
            ),
            'Tourtype':forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control'
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
                    'class': 'form-control'
                }
            ),
            'BriefContent':forms.Select(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control'
                }
            ),
            'HashTag':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control',
                    'placeholder' : 'Ex) #Seoul #hiking #bicycle #picnic #localfood #picture #exercise #beer'
                }
            ),
            'MeetingPoint':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control',
                    'placeholder': 'Ex) 94, Wausan-ro Mapo-gu Seoul'
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
                    'placeholder': 'Ex) 3hr 30min'
                }
            ),
            'Price':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray; margin-bottom:8px;',
                    'class': 'form-control'
                }
            ),
            'Minimum' : forms.NumberInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'Maximum': forms.NumberInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'Price_include':forms.Textarea(
                attrs={
                    'style': 'width:100%; height:130px; margin-top:4px; border:1px solid gray;',
                    'placeholder' : 'Ex) traditional market, bicycle rental, Gyengbuk palace entree, dinner, lunch',
                    'class': 'form-control'
                }
            ),
            'NotDate':DatePickerWidget(
                attrs={
                    'style':'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'GuestInfo':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:130px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'img':forms.ClearableFileInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'SeasonFrom': DatePickerWidget(
                attrs={
                    'style':'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'SeasonTo': DatePickerWidget(
                attrs={
                    'style':'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'CourseName': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'DurationCourse': forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px;border:1px solid gray;',
                    'class': 'form-control'
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
                    'class': 'form-control'
                }
            )
        }

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post






class BookMForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'NOP': forms.NumberInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'LastName': forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'FirstName': forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Age': forms.NumberInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'

                }
            ),
            'gender': forms.Select(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Email': forms.EmailInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Date': DatePickerWidget(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control',
                    'multiple': True

        }
            ),
            'SNS': forms.Select(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Nationality': AutoCompleteSelect(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control',
                    'multiple': True
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'ConfirmedEmail': forms.EmailInput(
                attrs={
                    'style':'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Language': forms.Select(
                attrs={
                    'style': 'border:1px solid gray; height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'SNSID': forms.TextInput(
                attrs={
                    'style': 'border:1px solid gray;height:27px;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
            'Demand': forms.Textarea(
                attrs={
                    'style': 'width:100%; height:27px; border:1px solid gray;margin-top:3px;',
                    'class': 'form-control'
                }
            ),
        }

    def save(self, **kwargs):
        post = super().save(commit=False)
        post.author = kwargs.get('content', None)
        post.save()

        return post