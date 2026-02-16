from django.shortcuts import render,HttpResponse,redirect
from .models import Employee
from .forms import EmployeeForm,CourseForm

# Create your views here.
def employeeList(request):
    #employees = Employee.objects.all() #select * from employee
    employees = Employee.objects.all().order_by("id").values()
    #employees = Employee.objects.all().values_list()
    print(employees)
    return render(request, 'employee/employeeList.html',{"employees":employees})


def employeeFilter(request):
    #where select  from employee where name = "Vraj"
    employee = Employee.objects.filter(name ="Vraj").values()
    #selet  from employee where post = "Analyst"
    employee2 = Employee.objects.filter(post ="Analyst").values()
    #select  from employee where name = "Darshan" and post = "Developer"
    employee3 = Employee.objects.filter(name ="Darshan",post ="Analyst").values()
    #select  from employee where name = "Darshan" or post = "Developer"

    #>22
    #select  from employee where age > 22
    #employee4 = Employee.objects.filter(age>2).values()
    employee4 = Employee.objects.filter(age__gt=22).values()
    employee5 = Employee.objects.filter(age__gte=22).values() #select  from employee where age >= 22

    #lt , lte

    #string queries
    employee6 = Employee.objects.filter(post__exact="Analyst").values()  #case sensitive (will find exact name "Analyst" but not "analyst")
    employee7 = Employee.objects.filter(post__iexact="analyst").values() #select  from employee where post = "analyst" or post = "Analyst" means case insensitive
    #contains
    employee8 = Employee.objects.filter(name__contains="r").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="V").values()
    employee11 = Employee.objects.filter(name__endswith="D").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="N").values()

    #in
    employee14 = Employee.objects.filter(name__in=["raj","Vraj"]).values()   #select  from employee where name in ("raj","Vraj") means name = "raj" or name = "Vraj" 

    #range
    employee15 = Employee.objects.filter(age__range=[23,30]).values()    

    #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()    #desc


    #and
    print("query 1",employee) 
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
    print("query 18",employee18)
    return render(request, 'employee/employeeFilter.html') # rendering the html page employeeFilter.html

def createEmployee(request):    
    Employee.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date="2022-01-01")
    return HttpResponse("EMPLOYEE CREATED...")

def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() #it same as create
        return redirect("employeeList")
    else:
        #form object create --> html
        form = EmployeeForm() #form object        
        return render(request,"employee/createEmployeeForm.html",{"form":form})

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("COURSE CREATED...")
    else:
        form = CourseForm()
        return render(request,"employee/createCourse.html",{"form":form})

def deleteEmployee(request,id):
    #delete from employees where id = 1
    print("id from url = ",id)
    Employee.objects.filter(id=id).delete()
    #return HttpResponse("EMPLOYEE DELETED...")
    #employee list redirecr
    return redirect("employeeList") #url --> name --> 

def filterEmployee(request):
    print("filter employee called...")
    employees = Employee.objects.filter(age__gte=25).values()
    print("filter employees = ",employees)
    #return redirect("employeeList")
    return render(request,"employee/employeeList.html",{"employees":employees})

def sortemployees(request, id):
    if id == 1:
        employees = Employee.objects.order_by("age").values()    #ascending
    elif id == 2:
        employees = Employee.objects.order_by("-age").values()   #descending
    else:
        employees = Employee.objects.all().values()  # Default (no sorting)
    return render(request,"employee/employeeList.html",{"employees":employees})

#update --->
def updateEmployee(request,id):
    #database existing user... id -->
    employee = Employee.objects.get(id=id) #select * from employee where id = 1
    
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        form.save()
        return redirect("employeeList")
    else:
        form = EmployeeForm(instance=employee)    
        return render(request,"employee/updateEmployee.html",{"form":form})
