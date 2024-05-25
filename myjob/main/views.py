from django.shortcuts import render
from .models import Skils
from .models import Image

# Create your views here.
def index(request):
    skill = Skils.objects.all()
    image = Image.objects.all()
    return render(request, 'main/index.html', {'skill': skill, 'image': image})

def index_ua(request):
    return render(request, 'main/base_ua.html')

def index_de(request):
    return render(request, 'main/base_de.html')

def arts(request):
    image = Image.objects.all()
    return render(request, 'main/arts.html', {'image': image})

