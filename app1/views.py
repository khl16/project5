
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    if "counter" in request.session:
        counter = request.session["counter"]
    else:
        counter = 0
        request.session["counter"] = 0

    request.session["counter"] = counter +1


    context= {
            "counter":counter

    }

    return render (request, 'index.html',context=context)


def delindex(request):
    del request.session['counter']
    return redirect('/')
    


