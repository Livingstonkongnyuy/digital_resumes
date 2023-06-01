from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2',)


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)      #overwirte
        
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserSigninForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')   

    def __init__(self, *args, **kwargs):
        super(UserSigninForm, self).__init__(*args, **kwargs)      #overwirte
    
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None  

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class Add_profileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

        
class TestimoniesForm(forms.ModelForm):
    class Meta:
        model = Testimonies
        fields = '__all__'


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = '__all__'


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
