from django.urls import path
from . import views

app_name = 'Login'
urlpatterns = [
    path('login/', views.do_login, name='do_login'),
    path('logout/', views.do_logout, name='do_logout'),
    path('cadastro/', views.casdastro, name='cadastro')
]
