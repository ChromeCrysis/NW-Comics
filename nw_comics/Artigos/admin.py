from django.contrib import admin
from .models import Artigos

# Register your models here.

class ArtigosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Artigos, ArtigosAdmin)