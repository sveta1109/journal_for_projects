from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
def project_list(request):
    all_projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': all_projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_details.html', {'project': project})


def chapter_detail(request):
    return render(request, 'projects/chapter_detail')


def toggle_task(request):
    return render(request, 'projects/toggle_task')