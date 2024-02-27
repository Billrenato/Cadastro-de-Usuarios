from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')


def usuarios(request):
    # salaver os dados na tela do banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # exibir todoas usuarios
    usuarios = {
        'usuarios':Usuario.objects.all()
    }
    # retornar todo os dados para a pagina de listagem 
    return render(request,'usuarios/usuarios.html',usuarios)

      

