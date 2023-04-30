from django.shortcuts import render
from django.http import HttpResponse
import jwt
from .models import User
from datetime import datetime, timedelta
# Create your views here.
from django.http import HttpResponseRedirect
import json
from products.models import Products


def cart(request):
    token = request.COOKIES.get('username')
    cart = request.COOKIES.get('cart')
    if token:
        try:
            decoded_token = jwt.decode(token, 'djangojwt', algorithms=['HS256'])
            response = HttpResponse(render(request, 'pages/cart.html'))
            if cart == None:
                response.set_cookie('cart', [],max_age=604800)
            else:
                list = json.loads(cart)
                products = []
                for id in list:
                    product = Products.objects.get(id=id)
                    products.append(product)
                total_price = sum(product.price for product in products)
                context = {'data': products,'total_price':total_price}
                response = HttpResponse(render(request, 'pages/cart.html',context))
        except jwt.ExpiredSignatureError:
            response = HttpResponseRedirect('/user/signin')
    else:
        response = HttpResponseRedirect('/user/signin')
        
    
    
    return response

def deleteProduct(request,id):
    cart = request.COOKIES.get('cart')
    response = HttpResponse(render(request, 'pages/delete.html'))
    if request.method == 'POST' and 'yes' in request.POST:
        cart = request.COOKIES.get('cart')
        list = json.loads(cart)
        list.remove(id)
        response = HttpResponseRedirect('/user/cart')
        response.set_cookie('cart', list,max_age=604800)
    return response


def signin(request):
    message = ''
    
    if request.method == 'POST' and 'signin' in request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            
            if password == user.password:
                payload = {
                    'email': user.email,
                    'exp': datetime.utcnow() + timedelta(days=1),
                }
                token = jwt.encode(payload, "djangojwt", algorithm='HS256')
                response = HttpResponseRedirect('/')
                response.set_cookie('username', token, max_age=604800)
                return response
            else:
                message = 'Incorrect account or password information'
        except:
            message = 'Incorrect account or password information'
    response = HttpResponse(
        render(request, 'pages/signin.html', {'message': message}))
    return response


def checkVali(value):
    errorM = 'style="border: 1px solid red;"'
    successM = 'style="border: 1px solid green;"'
    if value.strip() == '':
        return errorM
    else:
        return successM


def signup(request):
    message = ""

    nameM = ''
    passwordM = ''
    passwordCM = ''
    emailM = ''
    ageM = ''

    if request.method == 'POST' and 'signup' in request.POST:
        name = request.POST.get('name')
        password = request.POST.get('password')
        passwordC = request.POST.get('passwordC')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        nameM = checkVali(name)
        passwordM = checkVali(password)
        passwordCM = checkVali(passwordC)
        emailM = checkVali(email)
        ageM = checkVali(age)
        if len(name) < 6 or len(name) > 20:
            message = 'Name length needs 6 to 20 characters'
        elif len(password) < 6 or len(password) > 20:
            message = 'Password length needs 6 to 20 characters'
        elif password != passwordC:
            message = 'Password and Password Confirm must be the same'
        else:
            try:
                User.objects.get(email=email)
                message = 'Email already exists'
            except:
                if (gender == None):
                    gender = False
                    new_user = User(name=name, password=password,
                                    email=email, age=age, gender=gender)
                else:
                    gender = True
                    new_user = User(name=name, password=password,
                                    email=email, age=age, gender=gender)
                message = 'You have successfully registered'
                new_user.save()
    response = HttpResponse(render(request, 'pages/signup.html', {
                            'message': message, 'name': nameM, 'password': passwordM, 'passwordC': passwordCM, 'email': emailM, 'age': ageM}))
    return response
