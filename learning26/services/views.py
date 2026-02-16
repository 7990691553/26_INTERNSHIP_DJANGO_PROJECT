from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.
def serviceList(request):
    services = Service.objects.all()
    return render(request, 'services/serviceList.html', {"services":services})

def createService(request):
    
    if request.method == "POST":
        form = ServiceForm(request.POST)

        if form.is_valid():
          form.save() #it same as create
          return redirect("serviceList")
    
    else:
        #form object create --> html
        form = ServiceForm() #form object    

    return render(request,"services/createService.html",{"form":form})