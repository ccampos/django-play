from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    templatename = 'MOAR.html'
    templatevars = {
        'blahblah': 'meaow'
    }
    return render(request, templatename, templatevars)
    # return HttpResponse('Hello World!')