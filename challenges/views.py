from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect

monthly_challenges_dict = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 min every day!",
    "march": "Learn Django everday for 20 min!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 min every day!",
    "june": "Learn Django everday for 20 min!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 min every day!",
    "september": "Learn Django everday for 20 min!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 min every day!",
    "december": "Learn Django everday for 20 min!"
}


# Create your views here.
def monthly_challenge_by_no(request, month):
    months_list = list(monthly_challenges_dict.keys())
    # Logic is month as int is the argument we are getting here and we will put the value of redirect month using the
    # basic python list index value and method
    if month>len(months_list):
        return HttpResponseNotFound("Invalid Month!! Try Again")
    redirect_month = months_list[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
    except KeyError:
        return HttpResponseNotFound('This month is not supported')
    return HttpResponse(challenge_text)
