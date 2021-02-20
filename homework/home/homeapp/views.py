from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    q1 = (request.GET["a1"] == "4")
    q2 = (request.GET["a2"] == "1")
    score = q1 + q2
    return render(request, "result.html",{"q1":q1, "q2":q2, "score":score})