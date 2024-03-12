from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from.models import Product, Cart, Order
# Create your views here.

def index(req):
    allproducts = Product.objects.all() #to add all data on page
    context={"allproducts":allproducts}  #to call product data on page
    return render(req,'index.html',context) #add context on page

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def signup(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}

        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("/signin")
            except:
                context["errmsg"] = "User Already exists"
                return render(req, "signup.html", context)
    else:
        context = {}
        context["errmsg"] = ""
        return render(req, "signup.html", context)


from django.contrib.auth import authenticate, login, logout


def signin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        if uname == "" or upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signin.html", context)
        else:
            userdata = authenticate(username=uname, password=upass)
            if userdata is not None:
                login(req, userdata)
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(req, "signin.html", context)
    else:
        return render(req, "signin.html")


def userlogout(req):
    logout(req)
    return redirect("/")

def glasslist(req):
    if req.method == "GET":
        allproducts = Product.productmanager.glass_list()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)
    else:
        allproducts=Product.objects.all()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)
    
def shoeslist(req):
    if req.method == "GET":
        allproducts = Product.productmanager.shoes_list()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)
    else:
        allproducts=Product.objects.all()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)

def clothlist(req):
    if req.method == "GET":
        allproducts = Product.productmanager.cloth_list()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)
    else:
        allproducts=Product.objects.all()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)
    
def electronicslist(req):
    if req.method == "GET":
        allproducts = Product.productmanager.electronics_list()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)
    else:
        allproducts=Product.objects.all()
        context={"allproducts":allproducts}
        return render(req,'index.html',context)
    
def pricerangeview(req):
    if req.method == "GET":
        return render(req, "index.html")
    else:
        r1 = req.POST.get("min")
        r2 = req.POST.get("max")
        if r1 is not None and r2 is not None and r1.isdigit() and r2.isdigit():
            allproducts = Product.productmanager.getpricerange(r1, r2)
            context = {"allproducts": allproducts}
            return render(req, "index.html", context)
        else:
            allproducts = Product.objects.all()
            context = {"allproducts": allproducts}
            return render(req, "index.html", context)
        
def allsortedproducts(req):
    sortoption = req.GET.get("sort")
    if sortoption == "high_to_low":
        allproducts = Product.objects.order_by("-price") # dec order
    elif sortoption == "low_to_high":
        allproducts = Product.objects.order_by("price") # asc order
    else:
        allproducts = Product.objects.all()

    context={"allproducts":allproducts}
    return render(req,'index.html',context)

from django.db.models import Q

def serchproducts(req):
    query=req.GET.get("q")
    errmsg=""
    if query:
        allproducts=Product.objects.filter(
            Q(productname__icontains=query)
            |Q(desc__icontains=query)
            |Q(category__icontains=query)
            |Q(price__icontains=query)      
        )
        if len(allproducts)==0:
            errmsg="No products found"
    else:
        allproducts=Product.objects.all()

    context={"allproducts":allproducts, "errmsg":errmsg, "query":query}
    return render(req,'index.html',context)

def showcart(req):
    if req.user.is_authenticated:
        username = req.user.username
        allcarts = Cart.objects.filter(userid=req.user.id)
        # print(allcarts)
        totalamount = 0
        for x in allcarts:
            totalamount = totalamount + x.productid.price * x.qty

        totalitems = len(allcarts)
        context = {
            "allcarts": allcarts,
            "username": username,
            "totalamount": totalamount,
            "totalitems": totalitems,
        }
        return render(req, "showcart.html", context)
    else:
        allcarts = Cart.objects.filter(userid=req.user.id)
        # print(allcarts)
        totalamount = 0
        for x in allcarts:
            totalamount = totalamount + x.productid.price * x.qty

        totalitems = len(allcarts)
        context = {
            "allcarts": allcarts,
            "totalamount": totalamount,
            "totalitems": totalitems,
        }
        return render(req, "showcart.html", context)

def addtocart(req, productid):
    if req.user.is_authenticated:
        user = req.user
    else:
        user = None

    allproducts = get_object_or_404(Product, productid=productid)
    cartitem, created = Cart.objects.get_or_create(productid=allproducts, userid=user)
    if not created:
        cartitem.qty += 1
    else:
        cartitem.qty = 1
    cartitem.save()
    # msg = "Item added to Cart"
    # context = {"msg": msg}
    return redirect("/showcart")
    # return render(req, "index.html", context)

def removefromcart(req, productid):
    cartitem = Cart.objects.filter(productid=productid)
    cartitem.delete()
    return redirect("/showcart")

def updateqty(req, qv, productid):
    allcarts = Cart.objects.filter(productid=productid)
    if qv == 1:
        total = allcarts[0].qty + 1
        allcarts.update(qty=total)
    else:
        if allcarts[0].qty > 1:
            total = allcarts[0].qty - 1
            allcarts.update(qty=total)
        else:
            allcarts = Cart.objects.filter(productid=productid)
            allcarts.delete()

    return redirect("/showcart")

import razorpay

import random

import random


def payment(req):
    if req.user.is_authenticated:
        user = req.user
        client = razorpay.Client(
            auth=("rzp_test_aEn50t5loPG11D", "LWaRX6NXzdsapNGUUYMlfaEi")
        )
        allcarts = Cart.objects.filter(userid=user)

        for x in allcarts:
            orderid = random.randrange(1000, 90000)
            orderdata = Order.objects.create(
                orderid=orderid, productid=x.productid, qty=x.qty, userid=x.userid
            )
            orderdata.save()
            x.delete()

        totalamount = 0
        orderdata = Order.objects.filter(userid=user)
        for x in orderdata:
            totalamount = totalamount + x.qty * x.productid.price
            oid = x.orderid

        data = {
            "amount": totalamount * 100,
            "currency": "INR",
            "receipt": str(oid),
        }
        payment = client.order.create(data=data)
        context = {"data": payment, "amount": payment, "username": user}
        return render(req, "payment.html", context)
    else:
        return redirect("/signin")
    

def showorders(req):
    if req.user.is_authenticated:
        user=req.user
        orderdata=Order.objects.filter(userid=user) 
        context={"username":user,"orderdata":orderdata}
        return render(req,"showorders.html",context) 
