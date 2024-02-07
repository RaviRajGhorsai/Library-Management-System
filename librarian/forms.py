from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
    
class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book_id', 'borrower_id']
        
class BookSearchForm(forms.Form):
    book = forms.CharField(label='Book', required=False)
    genre = forms.CharField(label='Genre', required=False)
    author = forms.CharField(label='Author', required=False)