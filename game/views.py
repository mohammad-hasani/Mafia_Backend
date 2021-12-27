from django.shortcuts import render

# Create your views here.


def admin(request):
    return render(request, "admin_page.html", {})


def user(request):
    return render(request, "user_page.html", {})