from .backend import MyBackend
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.

def do_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verifica o usuario
        if MyBackend.checkUser(username=username) == False:
            messages.warning(request, 'Usuario ou senha incorreto!')
            return render(request, 'login.html')
        else:
            # Verifica a senha
            if MyBackend.checkPassword(username=username, password=password) == False:
                messages.warning(request, 'Usuario ou senha incorreto!')
                return render(request, 'login.html')
            else:
                user = MyBackend.authenticate(username=username, password=password)
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('Home:index')

def do_logout(request):
    logout(request)
    return redirect('Home:index')

def casdastro(request):
    pass