from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(Request):
    ENTETE="Salut"
    fin="aurevoir"
    return HttpResponse(ENTETE+fin)

def nb(request,n):
    context={'Title':n}
    return render(request,'quiz/index.html',context)