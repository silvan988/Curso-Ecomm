from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar pedido')


class FecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('fechar pedido')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe')
