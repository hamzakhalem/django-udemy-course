from django import forms

class newForm(forms.Form):
    title = forms.CharField(max_length=200, label="title", widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=200, label="subject", widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=200, label="email", widget=forms.Textarea(attrs={'class':'form-control'}))