"""Views for the store app."""

from django.shortcuts import render

from .models import Product

# Create your views here.
def storehome(request):
    # get the products from the database
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/storehome.html', context)

def aboutus(request):
    return render(request, 'store/aboutus.html', {'title': 'About Us'})

def reviews(request):
    return render(request, 'store/reviews.html', {'title': 'Reviews'})
