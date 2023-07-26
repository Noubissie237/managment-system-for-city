from django.shortcuts import render
from django.http import HttpResponse
from .models import Logement
from .models import Occuper

# Create your views here.

def logement(request):

    logementOcc = []
    logementTot = []
    logementDisp = []

    listeOcc = Occuper.objects.all().order_by('id_logement')
    listeTot = Logement.objects.all().order_by('id_logement')
    listeDisp = listeTot
    
    for elt in listeOcc:
        logementOcc.append(elt.id_logement)

    for elt in listeTot:
        logementTot.append(elt)

    for elt in listeDisp:
        logementDisp.append(elt)

    for elt in logementDisp:
        for check in logementOcc:
            if(elt == check):
                logementDisp.remove(elt)

    dataset = {
        'listTot' : logementTot,
        'nbreT' : len(logementTot),
        'listOcc' : logementOcc,
        'nbreO' : len(logementOcc),
        'listDisp' : logementDisp,
        'nbreD' : len(logementDisp) 
    }

    return render(request, 'index.html', dataset)
    