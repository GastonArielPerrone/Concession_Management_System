from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            # Usamos el backend de autenticación que configuramos para que funcione con email
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Correo electrónico o contraseña incorrectos.')
        return cleaned_data
    
class CreateAccount(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', widget=forms.Textarea(attrs={"class": 'form-control', 'placeholder': 'Nombre'}))
    apellido = forms.CharField(label='Apellido',widget=forms.Textarea(attrs={"class": 'form-control', 'placeholder': 'Nombre'}))
    email = forms.EmailField(label='Correo Electronico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Confirmación de Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    is_active = forms.BooleanField(label='Empleado Activo') # type: ignore
    is_staff = forms.BooleanField(label='Staff Administrativo') # type: ignore
    