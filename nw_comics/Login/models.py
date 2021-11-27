from django.db import models

# Create your models here.

class Usuarios(models.Model):
    auth_user = models.OneToOneField('auth.User', on_delete=models.PROTECT, null=True)
    admin = models.BooleanField(default=False)
    ativado = models.BooleanField(default=False)
    data_nascimento = models.TextField()