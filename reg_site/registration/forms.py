from django import forms

class regform(forms.Form):
    Name = forms.CharField(label='name',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your name'}))
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    age = forms.IntegerField(label='age',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'your age'}))
    mobile = forms.IntegerField(label='mobile',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'mobile no.'}))
    password = forms.CharField(label='password',max_length=32,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

class searchingform(forms.Form):
    id = forms.IntegerField(label="Search info about an user by entering its id",widget= forms.NumberInput(attrs={'class':'form-control','placeholder':'enter a valid id here'}))
class deleteform(forms.Form):
    id  = forms.IntegerField(label="Enter a valid id to delete",widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'enter an id here'}))

class updateform(forms.Form):
    id  = forms.IntegerField(label='Enter a valid user id whose info you are trying to update',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'enter an id here to update'}))

