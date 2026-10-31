from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def project_list(request):
    return render(request, 'projects/project_list.html')


def project_detail(request):
    return render(request, 'projects/project_details.html')


def chapter_detail(request):
    return render(request, 'projects/chapter_detail')


def toggle_task(request):
    return render(request, 'projects/toggle_task')