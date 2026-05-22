from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista.html', {'produtos': produtos})
    
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
]

<h1>Produtos</h1>

<p>Relógio - R$ 250.00</p>
<p>Bota - R$ 180.00</p>

{% for produto in produtos %}
    <p>{{ produto.nome }} - R$ {{ produto.preco }}</p>
{% endfor %}