from django.shortcuts import render


def planning(request):
    return render(request, 'planning/planning.html')
