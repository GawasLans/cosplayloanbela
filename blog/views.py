from django.shortcuts import render
from .models import Cosplay
# Create your views here.

def index(request):
    # Filtramos las imágenes por categoría y tomamos las últimas 4 subidas
    loan_images = Cosplay.objects.filter(category='LOAN').order_by('-created_at')[:4]
    bela_images = Cosplay.objects.filter(category='BELA').order_by('-created_at')[:4]
    duo_images = Cosplay.objects.filter(category='DUO').order_by('-created_at')[:4]

    context = {
        'loan_images': loan_images,
        'bela_images': bela_images,
        'duo_images': duo_images,
    }
    return render(request, 'blog/index.html', context)
