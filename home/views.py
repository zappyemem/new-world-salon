from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return index page on home app """
    return render(request, "home/index.html")