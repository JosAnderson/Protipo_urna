from django.shortcuts import render
from .models import Candidato


def main(request):
    candidatos = Candidato.objects.all()
    dados = {
        'candidatos': candidatos
    }
    return render(request, 'main.html', dados)

def urnaForm(request):
    return render(request, "urna_Form.html")

