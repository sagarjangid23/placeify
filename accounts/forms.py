from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "block w-full px-3 py-1.5 text-gray-700 border rounded-md bg-gray-100 border-gray-600 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring",
                }
            )
            if field_name == "password1":
                field.widget.attrs["placeholder"] = "New password"
            elif field_name == "password2":
                field.widget.attrs["placeholder"] = "Confirm new password"
            else:
                field.widget.attrs["placeholder"] = f"Enter your {field_name}"

    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    place = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("name", "username", "age", "place", "password1", "password2")

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 13:
            raise forms.ValidationError(
                "You must be at least 13 years old to register."
            )
        return age


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "block w-full px-4 py-2 mt-2 text-gray-700 border rounded-md bg-gray-800 border-gray-600 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring",
                }
            )
            if field_name == "username":
                field.widget.attrs["placeholder"] = "Enter your username"
            elif field_name == "password":
                field.widget.attrs["placeholder"] = "Enter your password"

    class Meta:
        model = User
        fields = ("username", "password")


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "block w-full px-4 py-2 mt-2 text-gray-700 border rounded-md bg-gray-200 border-gray-600 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring",
                }
            )

    class Meta:
        model = Profile
        fields = {"name", "place", "age"}
