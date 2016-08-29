from django.shortcuts import render, get_object_or_404

from .models import Course

def cursos(request):
    context = {}
    cursos = Course.objects.all()
    context['cursos'] = cursos

    return render(request, "curso/cursos.html",context)
def details(request,slug):
    curso = get_object_or_404(Course, slug = slug)
    context = {
        'curso': curso
    }
    template_name = 'curso/details.html'
    return render(request, template_name,context)
