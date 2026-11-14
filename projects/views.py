from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Chapter


# Create your views here.
def project_list(request):
    all_projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': all_projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    all_chapters = Chapter.objects.all()
    return render(request, 'projects/project_detail.html', {'project': project}, {'chapters': all_chapters})


def chapter_detail(request):
    return render(request, 'projects/chapter_detail')


def toggle_task(request):
    return render(request, 'projects/toggle_task')