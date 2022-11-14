# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Statistics(UserCreationForm):
    gameid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Game ID",
                "class": "form-control"
            }
        ))
    goals = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Goals",
                "class": "form-control"
            }
        ))
    assists = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Assists",
                "class": "form-control"
            }
        ))
    saves = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Saves",
                "class": "form-control"
            }
        ))
    shots = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Shots",
                "class": "form-control"
            }
        ))
    mvps = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "MVPs",
                "class": "form-control"
            }
        ))
    wins = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Wins",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('gameid', 'goals', 'assists', 'saves', 'shots', 'mvps', 'wins')