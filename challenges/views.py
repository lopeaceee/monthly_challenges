from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def monthly_challenge_by_number(request, month):
    list_months = list(monthly_challenges.keys())

    if month > len(list_months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = list_months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

# any response code that starts with a 3 is called a redirect
# any response that starts with 2 or 200 is successful

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")


# sends back a response and what is written inside is the item
# however only adding this function,
# django has no chance of knowing when to call it
