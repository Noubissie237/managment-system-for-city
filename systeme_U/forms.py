from tkinter import Widget
from django.core import validators
from django import forms 
from .models import *

class Register_log(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["qrcode"].widget.attrs.update(display="none")

    TYPE_CHOICES = [
        ('individuel', 'Individuel'),
        ('collectif', 'Collectif'),
    ]
    
    ETAT_CHOICES = [('occupe', 'Occupé'),
        ('libre', 'Libre'),
        ]

    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select)
    etat = forms.ChoiceField(choices=ETAT_CHOICES, widget=forms.Select)
    


    #qrcode = forms.FileField(widget=forms.FileInput({ 'class':'zero'}), label='') 

    class Meta:
        model = Logement
        fields = ['type','numero','localisation','etat','qrcode']
        widgets = {
            'type':forms.TextInput(attrs={'class':'form-control'}),
            'qrcode':forms.FileInput(attrs={ 'required': False ,'class':'zero'}),
            'numero':forms.TextInput(attrs={'type': 'number', 'required': True ,'class':'form-control'}),
            'localisation':forms.TextInput(attrs={'class':'form-control'}),
            'etat':forms.TextInput(attrs={'class':'form-control'}),
        }