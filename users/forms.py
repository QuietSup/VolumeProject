import Volume.models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label = 'Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Rachel Roth',
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '************',
                "autocomplete": "new-password"
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '************',
                "autocomplete": "new-password"
            },
        )
    )
    class Meta:
        model = Volume.models.User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Rachel Roth',
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '************',
            }
        ),
    )
    class Meta:
        model = Volume.models.User
        fields = ['username', 'password']

class UpdateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['avatar'] = forms.ImageField(
            label='Avatar',
            required=False,
            widget=forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'px_image_Upload',
                    'accept': ".png, .jpg, .jpeg",
                }
            )
        )

        self.fields['username'] = forms.CharField(
            label='Username',
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': self.instance.username
                }
            )
        )

        self.fields['first_name'] = forms.CharField(
            label='First Name',
            required=False,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': self.instance.first_name
                }
            )
        )
        self.fields['last_name'] = forms.CharField(
            label='Last Name',
            required=False,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': self.instance.last_name
                }
            )
        )
        self.fields['email'] = forms.EmailField(
            label='Email',
            required=False,
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'value': self.instance.email
                }
            )
        )

    class Meta:
        model = Volume.models.User
        fields = ['avatar', 'username', 'first_name', 'last_name', 'email']