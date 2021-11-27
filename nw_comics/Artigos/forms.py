# Imports do Django
from django.forms import ModelForm

# Imports do mesmo App
from .models import Artigos


class ArtigosForm(ModelForm):
    class Meta:
        model = Artigos
        fields = '__all__'