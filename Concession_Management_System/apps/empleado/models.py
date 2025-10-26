from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# --- MODELO CARGO ---
class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# --- MANAGER PERSONALIZADO ---
class EmpleadoManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre=nombre, apellido=apellido, **extra_fields)
        usuario.set_password(password)  # Hashea la contraseña
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, nombre, apellido, password, **extra_fields)


# --- MODELO EMPLEADO ---
class Empleado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, null=False, blank=False, on_delete=models.CASCADE)

    # Campos de control del sistema
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    objects = EmpleadoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
