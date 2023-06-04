from django import forms
from Volume.models import Pin


class CreatePinForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget= forms.FileInput(
            attrs={
                'id': 'px_file',
                'class': 'px-input-file',
            }
        )
    )

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'e. g. Marioni with logo',
            }
        )
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your legendary description',
                'rows': '5',
            }
        )
    )

    class Meta:
        model = Pin
        fields = ['image', 'title', 'description']
