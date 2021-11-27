from django.urls import path
from . import views

app_name = 'Artigos'
urlpatterns = [
    path('', views.meus_artigos, name='meus_artigos'),
    path('publicar', views.publicar, name='publicar')
]
