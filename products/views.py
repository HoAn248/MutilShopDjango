from django.shortcuts import render 
from django.http import HttpResponse
from .models import Products
import json
# Create your views here.
def shop(request):
    product = {'data': Products.objects.all()}
    response = HttpResponse(render(request, 'pages/shop.html',product))
    return response

def detail(request,id):
    product = Products.objects.get(id=id)
    context = {'data': product}
    response = HttpResponse(render(request, 'pages/detail.html',context))
    cart = request.COOKIES.get('cart')
    if cart == None:
        response.set_cookie('cart', [],max_age=604800)

    if request.method == 'POST' and 'cart' in request.POST:
        cart = request.COOKIES.get('cart')
        list = json.loads(cart)
        list.append(id)
        response.set_cookie('cart', list,max_age=604800)
    return response
