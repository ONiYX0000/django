from django.contrib import admin
from .models import Jogo, Pedido, ItemPedido

admin.site.register(Jogo)
admin.site.register(Pedido)
admin.site.register(ItemPedido)