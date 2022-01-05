from django.shortcuts import render, redirect


# Create your views here.
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('Auth:login')
    return render(request, 'home.html', {"user": request.user})


def front_view(request):
    return render(request, 'front.html', {"user": request.user})
