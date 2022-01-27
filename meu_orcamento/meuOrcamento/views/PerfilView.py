from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def perfil_view(request, id=None):
    perfil=None
    if id is None and request.user.is_authenticated:
        perfil = User.objects.filter(username=request.user).first()
    elif id is not None:
        perfil = User.objects.filter(username__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to='/')

    context = {
        'perfil': perfil,
        'title': 'Perfil',
    }
    return render(request, template_name = 'Perfil/perfil.html', context=context)