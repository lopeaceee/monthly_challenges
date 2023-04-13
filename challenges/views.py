from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# def january(request):
    # return HttpResponse("Exercise daily for at least 30 minutes")

# def february(request):
    # return HttpResponse("Try to accomplish at least one Udemy course")

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Exercise daily for at least 30 minutes"
    elif month == "february":
        challenge_text = "Try to accomplish at least one Udemy course"
    elif month == "march":
        challenge_text = "Eat vegetables thrice per week."
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
    
 
# sends back a response and what is written inside is the item
# however only adding this function, 
# django has no chance of knowing when to call it