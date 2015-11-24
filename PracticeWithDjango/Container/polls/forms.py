from django import forms

class TextField(forms.Form):
	name = forms.CharField(widget=forms.Textarea)
	