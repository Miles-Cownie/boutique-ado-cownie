from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view to return the Shopping Bag page """

    return render(request, 'bag/bag.html')
