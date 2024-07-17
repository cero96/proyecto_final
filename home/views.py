from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_View(request):

    context={

        'mensaje':'Autos Disponibles',
        'auto_disponibles':[

            'camionetas',
            'sedanes',
            'todoterreno',
            'familiar',
            'trabajo',
            'viajes',

        ]

    }

    return render(request, 'index.html',context)
