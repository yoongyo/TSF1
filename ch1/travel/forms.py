from .models import Post,Country,TypeOfTour,City,Language
from django import forms
from .widgets import DatePickerWidget,AutoCompleteSelect
from django.core.urlresolvers import reverse_lazy
import sys
from .widgets import LocationWidget
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
                ajax_url=reverse_lazy('country_list'),
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
            'MeetingTime':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                    'placeholder': 'Ex) 17:00'
                }
            ),
            'Map': LocationWidget(

            ),
            'Direction':forms.Textarea(
                attrs={
                    'style': 'width:100%; height:130px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control',
                }
            ),
            'CourseName':forms.TextInput(
                attrs={
                    'style': 'width:100%; height:30px; margin-top:4px; border:1px solid gray;',
                    'class': 'form-control'
                }
            ),
            'Duration':forms.TextInput(
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
        }

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post



class PostForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px; '
            }
        )
    )
    Tourtype = forms.ModelChoiceField(
        queryset = TypeOfTour.objects.all(),
        widget= forms.Select(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    Country = forms.ModelChoiceField(
        queryset = Country.objects.all(),
        widget=AutoCompleteSelect(
            ajax_url=reverse_lazy('country_list'),
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    City = forms.ModelChoiceField(
        queryset = City.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    Language = forms.ModelChoiceField(
        queryset = Language.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    DetailContent = forms.CharField(
        max_length = 1200,
        widget=forms.Textarea(
            attrs={
                'style': 'width:100%; height:240px; margin-top:4px;',
                'placeholder': '당신이 만든 local 여행에 대한 설명을 자유롭게 작성해 주세요\n'
                'Tip. 당신의 Tour만이 가지고 있는 특징에 대해 설명해 주세요.외국인은 언제나 local다움과 funny한 상품을 찾고있습니다.'


            }
        )
    )
    BreifContent = forms.CharField(
        max_length = 250,
        widget=forms.Select(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    HashTag = forms.CharField(
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    img = forms.ImageField(
        widget=forms.Select(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    MeetingPoint = forms.CharField(
        max_length = 50,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    MeetingTime = forms.CharField(
        max_length = 30,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )

    Map = forms.CharField(max_length=10, widget=NaverMapPointWidget())

    Direction = forms.CharField(
        max_length = 200,
        widget=forms.Textarea(
            attrs={
                'style': 'width:100%; height:130px; margin-top:4px;'
            }
        )
    )
    CourseName = forms.CharField(
        max_length = 40,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    Duration = forms.CharField(
        max_length = 20,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    Price = forms.CharField(
        max_length = 10,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    Minimum = forms.IntegerField(
        min_value = 1,
        max_value = 20,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    Maximum = forms.IntegerField(
        min_value = 2,
        max_value = 20,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    Price_include = forms.CharField(
        max_length = 100,
        widget=forms.Textarea(
            attrs={
                'style': 'width:100%; height:130px; margin-top:4px;',
                'placeholder' : 'Ex) traditional market, bicycle rental, Gyengbuk palace entree, dinner, lunch'
            }
        )
    )
    GuestInfo = forms.CharField(
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:130px; margin-top:4px;'
            }
        )
    )
    img = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
            }
        )
    )
    NotDate = forms.DateField(
        widget=DatePickerWidget(
            attrs={
                'style':'width:100%; height:30px; margin-top:4px;'
            }
        )
    )