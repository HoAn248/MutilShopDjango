from django.shortcuts import render 
from django.http import HttpResponse 
from products.models import Products
# Create your views here.
def index(request):
    product = {'data': Products.objects.all()[:4]}
    response = HttpResponse(render(request, 'pages/home.html',product))
    return response
