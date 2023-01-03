from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to reuturn the Index page """

    return render(request, 'home/index.html')
