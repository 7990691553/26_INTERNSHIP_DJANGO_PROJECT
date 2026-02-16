from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.
def serviceList(request):
    services = Service.objects.all().order_by("id").values()
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

def deleteService(request,id):
    #delete from services where id = 1
    print("id from url = ",id)
    Service.objects.filter(id=id).delete()
    #return HttpResponse("SERVICE DELETED SUCCESSFULLY...")
    #employee list redirecr
    return redirect("serviceList") #url --> name -->

#update --->
def updateService(request,id):
    #database existing user... id -->
    service = Service.objects.get(id=id) #select * from service where id = 1
    
    if request.method == "POST":
        form = ServiceForm(request.POST,instance=service)
        form.save()
        return redirect("serviceList")
    else:
        form = ServiceForm(instance=service)    
        return render(request,"services/updateService.html",{"form":form})