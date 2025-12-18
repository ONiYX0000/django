from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html', {
        'page_title': 'Página Inicial',
        'page_description': 'Bem-vindo à ONYX'
    })


def jogos(request):
    return render(request, 'jogos.html', {
        'page_title': 'Códigos de Jogos',
        'page_description': 'Confira nossos jogos disponíveis'
    })


def giftcards(request):
    return render(request, 'giftcards.html', {
        'page_title': 'Gift Cards',
        'page_description': 'Escolha seu gift card'
    })


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(
                request,
                username=user_obj.username,
                password=senha
            )
        except User.DoesNotExist:
            user = None

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'login.html', {
        'page_title': 'Login',
        'page_description': 'Acesse sua conta'
    })


def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar_senha')

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        login(request, user)
        return redirect('home')

    return render(request, 'cadastro.html', {
        'page_title': 'Cadastro',
        'page_description': 'Crie sua conta ONYX'
    })


@login_required
def perfil(request):
    return render(request, 'perfil.html', {
        'page_title': 'Meu Perfil',
        'page_description': 'Gerencie suas informações'
    })


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from loja.models import Pedido

@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    
    return render(request, 'meus_pedidos.html', {
        'pedidos': pedidos,
        'page_title': 'Meus Pedidos',
        'page_description': 'Acompanhe seus pedidos realizados'
    })



def logout_view(request):
    logout(request)
    return redirect('login')

def promocoes(request):
    return render(request, 'promocoes.html', {
        'page_title': 'Promoções',
        'page_description': 'Não perca as ofertas imperdíveis da ONYX!'
    })

