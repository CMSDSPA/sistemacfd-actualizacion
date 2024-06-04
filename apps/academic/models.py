from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=150, verbose_name="Sede")
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

class Progresive_School(models.Model):
    name = models.CharField(max_length=150, verbose_name="Escuela Programa") 
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Escuela Programa"
        verbose_name_plural = "Escuela Programa"

class Training_Area(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ambito de Formacion")
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Ambito de Formacion"
        verbose_name_plural = "Ambitos de Formacion"

class Section(models.Model):
    acronym = models.CharField(max_length=10, verbose_name="Sigla", null=False, blank=False)
    name = models.CharField(max_length=100, verbose_name="Seccion", null=False, blank=False)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"

class In_Charge_Of(models.Model):
    name = models.CharField(max_length=150, verbose_name="A cargo de")
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "A cargo de"
        verbose_name_plural = "A cargo de"

class Supplier(models.Model):
    name = models.CharField(max_length=150, verbose_name="Proveedoredor")
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
class Type_Training_Action(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tipo de Accion")
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Tipo de Accion Formativa"
        verbose_name_plural = "Tipos de Accion Formativa"

class Teacher_Training(models.Model):
    id_duoc = models.CharField(max_length=12, verbose_name="ID DUOC")
    name = models.CharField(max_length=150, verbose_name="Nombre Acción Formativa")
    year = models.PositiveSmallIntegerField(verbose_name="Ano", null=False, blank=False)
    duration = models.FloatField(verbose_name="Duración", null=False, blank=False)
    observation = models.TextField(verbose_name="Observación", null=True, blank=True)
    itinerary = models.CharField(max_length=255, verbose_name="Itinerario", null=True, blank=True)
    CARACTERIZATION_CHOICES = [
        ('Habilitante', 'Habilitante'),
        ('Voluntario', 'Voluntario'),
        ('Obligatorio', 'Obligatorio'),
    ]
    STATE_CHOICES = [
        ('Participación', 'Participación'),
        ('Aprovado', 'Aprovado'),
        ('Reprobado', 'Reprobado'),
    ]
    PERIOD_CHOICES = [
        ('PRIMER SEMESTRE', 'PRIMER SEMESTRE'),
        ('SEGUNDO SEMESTRE', 'SEGUNDO SEMESTRE'),
        ('SR', 'SR'),
        ('TAV', 'TAV'),
    ]
    END_MONTH_CHOICES = [
        ('ENERO','ENERO'),
        ('FEBRERO','FEBRERO'),
        ('MARZO', 'MARZO'),
        ('ABRIL', 'ABRIL'),
        ('MAYO', 'MAYO'),
        ('JUNIO', 'JUNIO'),
        ('JULIO', 'JULIO'),
        ('AGOSTO', 'AGOSTO'),
        ('SEPTIEMBRE', 'SEPTIEMBRE'),
        ('OCTUBRE', 'OCTUBRE'),
        ('NOVIEMBRE', 'NOVIEMBRE'),
        ('DICIEMBRE', 'DICIEMBRE'),
        ('SR', 'SR'),
    ]
    POST_CHOICES = [
        ('COLABORADOR', 'COLABORADOR'),
        ('EXTERNO', 'EXTERNO'),
        ('DOCENTE', 'DOCENTE'),
        ('SR', 'SR'),   
    ]
    characterization = models.CharField(max_length=20, choices=CARACTERIZATION_CHOICES, verbose_name="Caracterización")
    state = models.CharField(max_length=20, choices=STATE_CHOICES, verbose_name="Estado")
    tranin_area = models.ForeignKey('Training_Area', on_delete=models.CASCADE, verbose_name="Ambito de Formacion")
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, verbose_name="Periodo")
    end_month = models.CharField(max_length=10, choices=END_MONTH_CHOICES, verbose_name="Mes de finalizacion")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, verbose_name="Seccion")
    in_charge_of = models.ForeignKey('In_Charge_Of', on_delete=models.CASCADE, verbose_name="A cargo de")
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, verbose_name="Proveedor")
    type_training_action = models.ForeignKey('Type_Training_Action', on_delete=models.CASCADE, verbose_name="Tipo de Accion Formativa")
    post_choice = models.CharField(max_length=15, choices=POST_CHOICES, verbose_name="Cargo")
    # datos fuera de excel
    created_at = models.DateTimeField(verbose_name="Fecha de creacion", null=True, blank=False)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualizacion", null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Accion Formativa"
        verbose_name_plural = "Accion Formativa"