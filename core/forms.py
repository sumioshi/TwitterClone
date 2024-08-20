from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control tweet-input',
                'placeholder': 'O que está acontecendo?',
                'rows': 3,
            }),
        }
