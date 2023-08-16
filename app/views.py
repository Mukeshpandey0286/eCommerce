
from django.shortcuts import render,HttpResponse
from django.views import View
from .models import Product, Cart, OrderPlaced, Customer
from .forms import CustomerRegistrationForm
from django.contrib import messages
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  laptops = Product.objects.filter(category='L')
  return render(request, "app/home.html", {'topwears': topwears, 'bottomwears' : bottomwears, 'mobiles':mobiles, 'laptops' : laptops})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailVeiw(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, "app/productdetail.html", {'product': product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')


def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category = 'M')
 elif data == 'REDMI' or data == 'Samsung' or data == 'OPPO':
  mobiles = Product.objects.filter(category = 'M').filter(brand = data)
 elif data == 'below':
   mobiles = Product.objects.filter(category = 'M').filter(selling_price__lt = 15000)
 elif data == 'above':
   mobiles = Product.objects.filter(category = 'M').filter(selling_price__gt = 14000)
 return render(request, 'app/mobile.html', {'mobiles': mobiles})

def laptop(request, data=None):
 if data == None:
  laptops = Product.objects.filter(category = 'L')
 elif data == 'Macbook' or data == 'HP' or data == 'Dell':
  laptops = Product.objects.filter(category = 'L').filter(brand = data)
 elif data == 'below':
   laptops = Product.objects.filter(category = 'L').filter(selling_price__lt = 70000)
 elif data == 'above':
   laptops = Product.objects.filter(category = 'L').filter(selling_price__gt = 70000)
 return render(request, 'app/laptop.html', {'laptops': laptops})


def top(request, data=None):
 if data == None:
  tops = Product.objects.filter(category = 'TW')
 elif data == 'Hilly' or data == 'gtw' :
   tops = Product.objects.filter(category = 'TW').filter(brand = data)

 return render(request, 'app/topwear.html', {'tops': tops})


def bot(request, data=None):
 if data == None:
  bots = Product.objects.filter(category = 'BW')
 elif data == 'Tommy' or data == 'gbw' :
   bots = Product.objects.filter(category = 'BW').filter(brand = data)

 return render(request, 'app/bottomwear.html', {'bots': bots})

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')


class CustomerRegistrationView(View):
  def get(self, request):
   form = CustomerRegistrationForm()
   return render (request, 'app/customerregistration.html', {'form': form})
    
  
  def post(self, request):
   form = CustomerRegistrationForm(request.POST)
   if form.is_valid():
    messages.success(request, 'Congratualation! You Successfully Registered.')
    form.save()
   return render (request, 'app/customerregistration.html', {'form': form})
    


def checkout(request):
 return render(request, 'app/checkout.html')
