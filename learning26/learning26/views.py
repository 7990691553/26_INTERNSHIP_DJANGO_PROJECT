from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("About")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def recap(request):
    return render(request,"recap.html")

def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredient} 
    return render(request,"recipe.html",data)

def team(request):
    team_name = "Royal Challengers Bengaluru"
    ipl_titles = 2   # change to 3 to see "Winners"

    players = [
        "Virat Kohli",
        "AB de Villiers",
        "Chris Gayle",
        "Mayank Agrawal",
        "Shane Watson",
        "Jacob Bethal",
        "Mohammad Siraj",
        "Bhuvneshwar Kumar",
        "Jasprit Bumrah",
        "Hardik Pandya",
        "Axar Patel"
    ]

    return render(request, "team.html", {
        "team_name": team_name,
        "ipl_titles": ipl_titles,
        "players": players
    })