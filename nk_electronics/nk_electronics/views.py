from django.shortcuts import render, redirect
from store.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from django.views.decorators.csrf import csrf_exempt
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def base(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id = uid)
    context = {"user": user}
    
    return render(request, "main/base.html", context)

def home(request):
    product = Product.objects.filter(status= "Publish" )
    context = {"product":product}
    return render(request, "main/index.html", context)

def product(request):
    
    categories = Category.objects.all()
    filter_price = Filter_price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    
    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    COLORID = request.GET.get('color')
    BRANDID = request.GET.get('brand')
    
    ATOZ = request.GET.get('ATOZ')
    ZTOA = request.GET.get('ZTOA')
    PRICE_LOWTOHIGH = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOW= request.GET.get('PRICE_HIGHTOLOW')
    SORT_NEW = request.GET.get('SORT_NEW')
    SORT_OLD = request.GET.get('SORT_OLD')
    
    if CATID:
        product = Product.objects.filter(Categories = CATID, status= "Publish")
    elif PRICE_FILTER_ID:
        product = Product.objects.filter(filter_price = PRICE_FILTER_ID, status= "Publish")
    elif COLORID:
        product = Product.objects.filter(color = COLORID, status= "Publish")
    elif BRANDID:
        product = Product.objects.filter(brand = BRANDID, status= "Publish")
        
    elif ATOZ:
        product = Product.objects.filter(status= "Publish").order_by('name')
    elif ZTOA:
        product = Product.objects.filter(status= "Publish").order_by('-name')
    elif PRICE_LOWTOHIGH:
        product = Product.objects.filter(status= "Publish").order_by('price')
    elif PRICE_HIGHTOLOW:
        product = Product.objects.filter(status= "Publish").order_by('-price')
    elif SORT_NEW:
        product = Product.objects.filter(status= "Publish", condition = "New").order_by('-id')
    elif SORT_OLD:
        product = Product.objects.filter(status= "Publish", condition = "old")        

    else:
        product = Product.objects.filter(status= "Publish" ).order_by('-id')
        
    
    context = {"product":product, "categories" : categories, "filter_price" : filter_price, "color" : color, "brand":brand}
    return render(request, "main/product.html", context)

def search(request):
    query = request.GET.get('query') 
    product = Product.objects.filter(status= "Publish", name__icontains = query) 
    context = {"product":product,}   
    return render(request, "main/search.html",context)

def product_details(request, id):
    prod = Product.objects.filter(status= "Publish", id = id).first() 
    context = {"prod":prod,}
    return render(request, "main/product_single.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact_us(name = name,email = email,subject = subject,message = message)
        
        subject = subject
        message = message + ", sent by \n" + email
        email_form = settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, email_form,["nkisnithinkumar@gmail.com"])
            contact.save()
            return redirect("home")
        except:
            return redirect("contact")
        
        
    return render(request, "main/contact.html")

def handel_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('login')
    return render(request, "registration/auth.html")

def handel_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, "registration/auth.html")


def handel_logout(request):
    logout(request)
    return redirect("login")



@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart/cart_details.html')

def checkout(request):
    amount_str = request.POST.get('amount')
    amount_flt = float(amount_str)  
    amount = int(amount_flt) 
    
    payment = client.order.create({"amount":amount, "currency":"INR", "payment_capture":"1"})
    order_id = payment['id']
    context = {"order_id":order_id, "payment":payment}
    return render(request, 'cart/checkout.html', context)

def placeorder(request):
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id = uid)
        
        cart = request.session.get('cart')
        
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postalcode = request.POST.get('postalcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        amount = request.POST.get('amount')
        
        order_id = request.POST.get('order_id')
        payment = request.POST.get('payment')
        
        context = {"order_id":order_id}
        
        order = Order(user = user, firstname = firstname, lastname = lastname, country = country, address = address,
                      city = city, state = state, postalcode = postalcode, phone = phone, email = email, 
                      additional_info = message, payment_id = order_id, amount = amount)
        order.save()
        
        for i in cart:
            a = int(cart[i]["price"])
            b = int(cart[i]["quantity"])
            total = a*b
            item = Order_item(user = user, order = order, product = cart[i]["name"], image = cart[i]["image"],
                              quantity = cart[i]["quantity"], price = cart[i]["price"], total = total)
            item.save()
        return render(request, 'cart/placeorder.html', context)
 
@csrf_exempt    
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key,val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        
        user = Order.objects.filter(payment_id = order_id).first()
        user.paid = True
        user.save()
                
        
    return render(request, 'cart/thank_you.html')


def your_order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id = uid)
    
    order = Order_item.objects.filter(user = user,)
    context = {"order":order}
    return render(request, 'main/your_order.html', context)