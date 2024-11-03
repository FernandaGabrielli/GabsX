from django import forms

class TweetForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'input-field',
            'placeholder': 'O que está acontecendo?',
            'rows': 3,  # ou outro valor que você desejar
        }),
        max_length=280,  # Limite de caracteres, se desejado
    )
