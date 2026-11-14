from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


# Create your views here.
def project_list(request):
    all_projects = Project.objects.all()
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
        else:
            form = ProjectForm()
    return render(request, 'projects/project_list.html', {'projects': all_projects, 'form': form})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


def chapter_detail(request):
    return render(request, 'projects/chapter_detail')


def toggle_task(request):
    return render(request, 'projects/toggle_task')