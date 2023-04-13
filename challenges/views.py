from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# def january(request):
# return HttpResponse("Exercise daily for at least 30 minutes")

# def february(request):
# return HttpResponse("Try to accomplish at least one Udemy course")

monthly_challenges = {
    "january": "Exercise daily for at least 30 minutes",
    "february": "Try to accomplish at least one Udemy course",
    "march": "Eat vegetables thrice per week",
    "april": "Create a new blog website",
    "may": "Read two books",
    "june": "Finish two more courses",
    "july": "Read two books",
    "august": "Run for at least a mile",
    "september": "Meditate for at least 10 minutes on a daily basis",
    "october": "Create a Spotify playlist",
    "november": "Exercise daily for at least 30 minutes",
    "december": "Avoid fatty foods as much as possible",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # "<li><a href="...">January</a></li>"<li><a href="...">February</a></li>

    response_data = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    list_months = list(monthly_challenges.keys())

    if month > len(list_months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = list_months[month-1]
    redirect_url = reverse("month-challenge", args=[redirect_month]) # it will create
    # /challenges/january

    return HttpResponseRedirect(redirect_url)

# any response code that starts with a 3 is called a redirect
# any response that starts with 2 or 200 is successful

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")


# sends back a response and what is written inside is the item
# however only adding this function,
# django has no chance of knowing when to call it
