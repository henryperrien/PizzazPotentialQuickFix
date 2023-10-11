from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import MenuItem, Cart, CartMenuItem
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm



class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)


class CarouselImage(View):
    def view_carousel(request):
        images = CarouselImage.objects.all()
        return render(request, 'customer/index.html', {'images': images})

def cart(request):
    
    cart = None
    cartmenuitems =[]

    if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            cartmenuitems = cart.cartmenuitems.all()
    
    context = {"cart": cart, "items": cartmenuitems}
    return render(request, 'customer/cart.html', context)

def add_to_cart(request):
        data = json.loads(request.body)
        item_id = data["id"]
        item = MenuItem.objects.get(id=item_id)

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            cartMenuItem, created = CartMenuItem.objects.get_or_create(cart = cart, MenuItem = item)
            cartMenuItem.quantity += 1
            cartMenuItem.save()
            print(cartMenuItem)
        
        return JsonResponse(item_id + " It is working", safe = False)

def deleteCartMenuItem(request, id):
     item = CartMenuItem.objects.get(id=id)
     item.delete()
     return redirect('cart')

def increaseQuantity(request, id):
     item = CartMenuItem.objects.get(id=id)
     item.quantity +=1
     item.save()
     return redirect('cart')

def decreaseQuantity(request, id):
     item = CartMenuItem.objects.get(id=id)
     if item.quantity > 1:
        item.quantity -=1
        item.save()
        return redirect('cart')
     
     return redirect('cart')

def login_user(request):
    if request.method == "POST":
          username = request.POST["username"]
          password = request.POST["password"]
          user = authenticate(request, username=username, password=password)
          if user is not None:
            login(request, user)
            return redirect('index')
          else:
            messages.success(request, ("There was an error logging in. Try again."))
            return redirect('login')
    else:
        return render(request, 'customer/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully Logged Out."))
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successful."))
            return redirect('index')
    else: 
        form = RegisterUserForm()

    return render(request, 'customer/register.html', {"form": form})

class PizzaQuiz(View):
    def view_quiz(self, request, *args, **kwargs):
        return(request, 'customer/pizzaquiz.html')