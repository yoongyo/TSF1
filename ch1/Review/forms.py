from .models import Review
from django import forms
class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'review1': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'review2': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'review3': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'review4': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'review5': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }