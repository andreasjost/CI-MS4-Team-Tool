from django.shortcuts import render


def coaching(request):
    return render(request, 'coaching/coaching.html')