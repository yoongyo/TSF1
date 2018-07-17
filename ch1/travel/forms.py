from .models import Post,Country,TypeOfTour,City,Language
from django import forms



class PostMForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget = forms.TextInput(
            attrs={
                'style': 'width:100%; height:30px; margin-top:4px;'
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
        widget=forms.Select(
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
                'style': 'width:100%; height:240px; margin-top:4px;'
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
    Map = forms.CharField(
        max_length=10,
        widget=forms.Textarea(
            attrs={
                'style': 'width:100%; height:230px; margin-top:4px;'
            }
        )
    )
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
        widget=forms.TextInput(
            attrs={
                'style': 'width:100%; height:130px; margin-top:4px;'
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

class PostForm(forms.ModelForm):
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
        ]

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
