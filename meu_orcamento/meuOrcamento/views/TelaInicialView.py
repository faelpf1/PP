from django.http import HttpResponse

def tela_inicial_view(request):
    return HttpResponse("<h1>tela inicial</h1>")