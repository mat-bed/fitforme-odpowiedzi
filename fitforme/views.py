from django.shortcuts import render
from .models import Exercise
# Create your views here.
def zadanie1(request):
    return render(request, 'zadanie1.html')
def zadanie3(request):
    context = {
        "exercises": Exercise.objects.all()
    }
    return render(request, 'zadanie3.html', context)