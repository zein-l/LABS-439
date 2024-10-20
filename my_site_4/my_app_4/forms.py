from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email_address = forms.EmailField(label='Email Address')
    profession = forms.CharField(label='Profession', max_length=100)
    tel_number = forms.CharField(label='Number', max_length=15)
    address = forms.CharField(label='Address', max_length=200)
   
