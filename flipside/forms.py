from django import forms

class Form(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your Email', max_length=100)
    message = forms.CharField(label='Message', max_length=500)

