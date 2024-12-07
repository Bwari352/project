from django import forms
from .models import Customer, User, Category
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DataForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'insurance_duration': DatePickerInput(),
        }


class CreateAccount(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'})

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def __init__(self, *args, **kwargs):
        super(CreateAccount, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs ['class'] = 'form-control'
        self.fields['email'].widget.attrs ['placeholder'] = 'Email'
        self.fields['email'].label =''
        self.fields['email'].help_text = '<span class = "form-text text-muted"><small>Required.150 characters, digits and @/./+/-/_ characters.</small></span>'

        self.fields['username'].widget.attrs ['class'] = 'form-control'
        self.fields['username'].widget.attrs ['placeholder'] = 'Username'
        self.fields['username'].label =''
        self.fields['username'].help_text = '<span class = "form-text text-muted"><small>Required.150 characters, digits and @/./+/-/_ characters.</small></span>'




        self.fields['password'].help_text = '<ul class= "form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li></ul>'


