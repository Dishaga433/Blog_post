from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import LoginRegister, SellerRegistration, CustomerRegistration, Blogging
from new_app.models import Seller, Blog


# Create your views here.
def logi(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")


def dash(request):
    return render(request,"dashboard.html")


def SellerR(request):
    form1 = LoginRegister()
    form2=SellerRegistration()

    if request.method=="POST":
        form1 = LoginRegister(request.POST)
        form2=SellerRegistration(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1=form1.save(commit=False)
            user1.is_seller=True
            user1.save()
            user2=form2.save(commit=False)
            user2.user=user1
            user2.save()
            return redirect("login")


    return render(request,"seller_registration.html",{"form1":form1,"form2":form2})



def CustomerR(request):
    form1 = LoginRegister()
    form2=CustomerRegistration()

    if request.method=="POST":
        form1 = LoginRegister(request.POST)
        form2=CustomerRegistration(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1=form1.save(commit=False)
            user1.is_customer=True
            user1.save()
            user2=form2.save(commit=False)
            user2.user=user1
            user2.save()
            return redirect("login")


    return render(request,"customer_registration.html",{"form1":form1,"form2":form2})


def Login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        print(username)
        print(password)

        user=authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            if user.is_staff:
                print("admin")
                return redirect("dash")

            elif user.is_seller:
                print("admin")
                return redirect("dash")

            elif user.is_customer:
                print("admin")
                return redirect("dash")

        else:
            messages.info(request,'invalid credentials')
    return render(request,"login.html")






def blog_posting(request):
    data=Blogging()
    user1=request.user
    print(user1)
    rcvr=Seller.objects.get(user=user1)
    print(rcvr.id)
    if request.method == "POST":
        rname = Blogging(request.POST,request.FILES)
        if rname.is_valid():
            obj=rname.save(commit=False)
            obj.seller_name=rcvr
            obj.save()
            return redirect('table')
    return render(request,"blog.html",{"form":data})




def table(request):
    data = Blog.objects.all()
    return render(request, "blog_view.html", {'data': data})


def rmv(request, id):   #request delete aakkan
    data = Blog.objects.get(id=id)
    data.delete()
    return redirect("table")



def update(request, id):
    data = Blog.objects.get(id=id)
    form = Blogging(instance=data)
    if request.method == "POST":
        blood = Blogging(request.POST, instance=data)
        if blood.is_valid():
            blood.save()
        return redirect("table")
    return render(request, "update.html", {"form": form})
