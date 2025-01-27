from django.shortcuts import render
from .models import PorfolioForm
# Create your views here.
def porfolio(request):
    models = PorfolioForm.objects.all()
    return render(request, 'core/porfolio.html', {'models': models})