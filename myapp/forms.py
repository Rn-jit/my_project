from django import forms
from myapp.models import Madlib, Madlib2


class MadlibForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    container = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    adj1 = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    adj2 = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    adj3 = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    noun = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    animal = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    veg1 = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    veg2 = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    color = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))

    class Meta:
        model = Madlib
        fields = [
            'name',
            'container',
            'adj1',
            'adj2',
            'adj3',
            'noun',
            'animal',
            'veg1',
            'veg2',
            'color'
        ]


class Madlib2Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    adj1 = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    adj2 = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    body_part = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    noun = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    animal = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    verb = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))

    class Meta:
        model = Madlib2
        fields = [
            'name',
            'adj1',
            'adj2',
            'body_part',
            'noun',
            'animal',
            'verb'
        ]
