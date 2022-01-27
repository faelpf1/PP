from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from meuOrcamento.forms.AuthForm import LoginForm, RegisterForm

def login_view(request):
    loginForm = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/orcamento')

    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/")
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorretos'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }

    return render(request, template_name='Perfil/autenticacao.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    registerForm = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/orcamento')

    if request.method == 'POST':
        usuario = request.POST['usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            verifyUsuario = User.objects.filter(username=usuario).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUsuario is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este username!' }
            elif verifyEmail is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este e-mail!' }
            else:
                user = User.objects.create_user(usuario, email, senha)
                if user is not None:
                    message = { 'type': 'success', 'text': 'Conta criada com sucesso!' }
                else:
                    message = { 'type': 'danger',  'text': 'Um erro ocorreu ao tentar criar o usuário.' }

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Voltar para tela de login',
        'link_href': '/'
    }
    return render(request, template_name='Perfil/autenticacao.html', context=context)