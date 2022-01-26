from django.shortcuts import render, redirect, get_object_or_404
from meuOrcamento.models import Perfil
from meuOrcamento.forms.PerfilForm import PerfilForm, UserForm


def perfil_view(request, id=None):
    perfil=None

    if id is None and request.user.is_authenticated:
        perfil = Perfil.objects.filter(usuario=request.user).first()
    elif id is not None:
        perfil = Perfil.objects.filter(usuario__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to='/')

    context = {
        'perfil': perfil,
    }
    
    return render(request, template_name = 'perfil.html', context=context)


def editar_perfil(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    emailUnused = True
    message = None
    
    if request.method == 'POST':
        perfilForm = PerfilForm(request.POST, request.FILES, instance=perfil)
        userForm = UserForm(request.POST, instance=request.user)

        # Verifica se o e-mail que o usuário está tentando utilizar em seu perfil já existe em outro perfil
        verifyEmail = Perfil.objects.filter(usuario__email=request.POST['email']).exclude(usuario__id=request.user.id).first()
        emailUnused = verifyEmail is None
    else:
        perfilForm = PerfilForm(instance=perfil)
        userForm = UserForm(instance=request.user)

    if perfilForm.is_valid() and userForm.is_valid() and emailUnused:
        perfilForm.save()
        userForm.save()
        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
    else:
        if request.method == 'POST':
            if emailUnused:
                message = { 'type': 'danger', 'text': 'Dados inválidos' }
            else:  
                message = { 'type': 'warning', 'text': 'E-mail já usado por outro usuário' }
    
    context = {
        'perfilForm': perfilForm,
        'userForm': userForm,
        'message': message
    }

    return render(request, template_name='editarPerfil.html', context=context)