from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['gender', 'age', 'weight', 'height', 'activity']

class FoodForm(ModelForm):
    class Meta:
        model=Food
        fields="__all__"
