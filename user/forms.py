#USER FORMS:
#    LOGIN
#    REGISTER

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(max_length=20, label="password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="confirm", widget=forms.PasswordInput)
    
    def clean(self):  #form un içindeki bir method, biz override ediyoruz.
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and confirm != password:
            raise forms.ValidationError("Passwords dont match")
        
        values = {
            "username" : username,
            "password" : password,
        }

        return values