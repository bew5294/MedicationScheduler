from django.shortcuts import render, redirect
import json


# Create your views here.
def home_view(request):
    # example
    events = [{"id": 'a', "title": 'my event', "start": "2022-01-06", "end": "2022-01-08", "description": 'This is a cool event'}, {"id": 'b', "title": 'my event 2', "start": "2022-01-08", "description": 'This is a cool event 2'}]
    if not request.user.is_authenticated:
        return redirect('Auth:login')
    return render(request, 'home.html', {"user": request.user, "events": json.dumps(events)})


def front_view(request):
    return render(request, 'front.html', {"user": request.user})
