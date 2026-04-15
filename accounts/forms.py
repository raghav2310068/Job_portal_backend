from .models import Users
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["name", "mobile_number", "email", "password", "role"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter name"}
            ),
            "mobile_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter mobile number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter email"}
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Enter password"}
            ),
            "role": forms.Select(attrs={"class": "form-control"}),
        }
