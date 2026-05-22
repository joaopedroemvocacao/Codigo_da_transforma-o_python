from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    busca = request.GET.get('busca')

    if busca:
        produtos = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos = Produto.objects.all()

    return render(request, 'lista.html', {'produtos': produtos})