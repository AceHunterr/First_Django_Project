from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def jan(request):
#     return HttpResponse("Eat no meat for the entire month!")
# def feb(request):
#     return HttpResponse("Walk for at least 20 min every day!")


def monthly_challenge(request, month):
    challenge_text = ""
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    if month == "february":
        challenge_text = "Walk for at least 20 min every day!"
    return HttpResponse()
