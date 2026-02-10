from django.shortcuts import render
from .models import Employee

# Create your views here.
def employeeList(request):
    #employees = Employee.objects.all() #select * from employee
    employees = Employee.objects.all().values()
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
