from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.academic.models import Campus, Progresive_School, Teacher_Training

class CustomUser(AbstractUser):
    personal_number = models.CharField(max_length=15, verbose_name="Numero de personal", null=True, blank=False)
    rut = models.CharField(max_length=10, verbose_name="Rut", null=True, blank=False, unique=True)
    personal_number = models.CharField(max_length=15, verbose_name="Numero de personal", null=True, blank=False)
    rut = models.CharField(max_length=10, verbose_name="Rut", null=True, blank=False, unique=True)
    mother_surname = models.CharField(max_length=50, verbose_name="Apellido de la madre", null=True, blank=False)
    phone = models.IntegerField(verbose_name="Telefono", null=True, blank=True)
    birth_date = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=False)
    date_joined_duoc = models.DateField(verbose_name="Fecha de creacion", null=True, blank=False)
    # created_at = models.DateTimeField(verbose_name="Fecha de creacion", null=True, blank=False) consultar
    # updated_at = models.DateTimeField(verbose_name="Fecha de actualizacion", null=True, blank=False) consultar
    secondary_email = models.EmailField(verbose_name="Email secundario", null=True, blank=True)
    url_linkedin = models.URLField(verbose_name="URL de linkedin", null=True, blank=True)
    img_profile = models.ImageField(verbose_name="Imagen de perfil", null=True, blank=True, default="/img/profile.webp")
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('SE', 'Sin especificar'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, verbose_name="Genero", default="SE", null=True, blank=False)
    
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, verbose_name="Sede")
    progresive_school = models.ForeignKey(Progresive_School, on_delete=models.CASCADE, verbose_name="Escuela Programa")
    teacher_training = models.ManyToManyField(Teacher_Training, verbose_name="Formacion Docente")
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
