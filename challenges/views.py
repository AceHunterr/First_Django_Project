from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
    months_list = list(monthly_challenges_dict.keys())

    return render(request,"challenges/index.html",{
        "months": months_list,
    })

    # for month in months_list:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f'<li><a href="{month_path}"><h2>{capitalized_month}</h2></a></li>'
    # response_data = f"<h1>Choose the month for the daily challenge:</h1><hr><br><ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_no(request, month):
    months_list = list(monthly_challenges_dict.keys())
    # Logic is month as int is the argument we are getting here and we will put the value of redirect month using the
    # basic python list index value and method
    if month > len(months_list):
        return HttpResponseNotFound("Invalid Month!! Try Again")
    redirect_month = months_list[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:

        challenge_text = monthly_challenges_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
    except KeyError:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')
    # return HttpResponse(response_data)
