from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

    class Meta: 
        model = CustomUser
        fields = ("email",)


        #https://ordinarycoders.com/blog/article/django-user-register-login-logout

        #https://testdriven.io/blog/django-custom-user-model/