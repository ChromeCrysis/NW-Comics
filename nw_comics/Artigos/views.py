from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Artigos
from .forms import ArtigosForm

# Create your views here.

@login_required(login_url='Login:do_login')
def meus_artigos(request):
    artigos = Artigos.objects.filter(usuario=request.user)
    return render(request, 'meus_artigos.html', {'artigos' : artigos})

@login_required(login_url='Login:do_login')
def publicar(request):
    if request.method == 'GET':
        form = ArtigosForm()
        return render(request, 'publicar.html')
    elif request.method == 'POST':
        try:
            titulo = request.POST['titulo']
            resumo = request.POST['resumo']
            capa = request.POST['capa']
            
            artigo = Artigos(titulo=titulo, resumo=resumo, capa=capa, usuario=request.user)
            artigo.save()

            context = {
                'mensagem' : 'Artigo cadastrado com sucesso!'
            }
        except:
            context = {
                'mensagem' : 'Erro ao cadastrar o artigo!'
            }

        return render(request, 'publicar.html', context=context)
        

