from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    return render(request, "plantilla/base.html")

def salir(request):
    logout(request)
    return redirect("/")