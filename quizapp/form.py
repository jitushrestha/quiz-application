from django import forms
from django.db.models import fields
from quizapp.models import AdminLogin, Question, User


class quizappForm(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = ("username", "password")
        labels = {
            "username":"",
            "password":"",
        }
        widgets = { 
            "username":  forms.TextInput(attrs={'placeholder':'Admin Username','autocomplete': 'off', 'class':"form-control rounded-left"}), 
            "password": forms.PasswordInput(attrs={'placeholder':'Admin Password','autocomplete': 'off','data-toggle': 'password', 'class':"form-control rounded-left"}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = { 
            "question":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}), 
            "option1":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}), 
            "option2":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}), 
            "option3":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}), 
            "option4":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}), 
            "correctAns":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}),
            
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            "firstname":"",
            "lastname":"",
            "username":"",
            "password":"",
            "email":"",
            "contact":"",
            "image_url":"",
        }
        widgets = { 
            "firstname":  forms.TextInput(attrs={'placeholder':'Firstname','autocomplete': 'off', 'class':"form-control"}),
            "lastname":  forms.TextInput(attrs={'placeholder':'Lastname','autocomplete': 'off', 'class':"form-control"}),
            "username":  forms.TextInput(attrs={'placeholder':'Username','autocomplete': 'off', 'class':"form-control"}), 
            "password": forms.PasswordInput(attrs={'placeholder':'Password','autocomplete': 'off','data-toggle': 'password', 'class':"form-control"}),
            "email":  forms.TextInput(attrs={'placeholder':'Email','autocomplete': 'off', 'class':"form-control"}),
            "contact":  forms.TextInput(attrs={'placeholder':'Contact','autocomplete': 'off', 'class':"form-control"}),
            

        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")
        labels = {
            "username":"",
            "password":"",
        }
        widgets = { 
            "username":  forms.TextInput(attrs={'placeholder':'Username','autocomplete': 'off', 'class':"form-control rounded-left"}), 
            "password": forms.PasswordInput(attrs={'placeholder':'Password','autocomplete': 'off','data-toggle': 'password', 'class':"form-control rounded-left"}),
        }