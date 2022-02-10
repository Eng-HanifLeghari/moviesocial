from django import forms
from django.contrib.auth.models import User
from .models import Reviews
from django.contrib.auth.forms import UserCreationForm


class ReviewsForm(forms.ModelForm):
    rate = forms.Widget(attrs={'type': "hidden"})
    class Meta:
        model = Reviews
        fields = ['title', 'name', 'comment', 'rate']
        widgets = {'rate': forms.HiddenInput(),
                   'title': forms.TextInput(attrs={"class": 'form-control'}),
                   'name': forms.TextInput(attrs={"class": 'form-control'}),
                   'comment': forms.Textarea(attrs={"class": 'form-control'})},


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # password2 = forms.CharField(
    #     label=_("Password confirmation"),
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
    # )
    #
    # class Meta:
    #     model = User
    #     fields = ("username",)
    #     field_classes = {'username': UsernameField}