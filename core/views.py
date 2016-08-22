from django.shortcuts import render

def base(request):
    template_name = "core\index.html"
    return render(request,template_name)

def home(request):
    template_name = 'core\home.html'
    return render(request,template_name)
def cursos(request):
    template_name = 'core\cursos.html'
    return render(request,template_name)
def contato(request):
    template_name = 'core\contato.html'
    return render(request,template_name)


# Create your views here.
