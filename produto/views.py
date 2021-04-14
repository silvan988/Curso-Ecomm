from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe produto smf')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('adicionar carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('remover carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('finalizar')
