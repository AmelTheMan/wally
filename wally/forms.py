from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude =["post"]
        labels={
            "user_name": "Your Name",
            "text":"Your Comment"
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username", "email", "password1", "password2"]


