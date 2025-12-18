from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),

    path('jogos/', views.jogos, name='jogos'),
    path('giftcards/', views.giftcards, name='giftcards'),

    path('perfil/', views.perfil, name='perfil'),
    path('meus-pedidos/', views.meus_pedidos, name='meus_pedidos'),

    path('meus-pedidos/', views.meus_pedidos, name='meus_pedidos'),
    path('promocoes/', views.promocoes, name='promocoes'),
]
