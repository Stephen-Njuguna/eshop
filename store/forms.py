from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#User modification to include emails 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
#user subcription form 

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=30, label='User name')
    email = forms.EmailField(label='Email')