from django.shortcuts import render, HttpResponse, redirect
from bhptale.models import RoleDetails
from django.contrib.auth.hashers import make_password,check_password
from Misc.generic import random_string, link_sending
import datetime as dt


from django.core.files.storage import FileSystemStorage

# Create your views here.
def sign_in(request):
    if(request.method=="POST"):
        useremail=request.POST["email"]
        passwd=request.POST["password"]
        data=RoleDetails.objects.get(email=useremail)
        if(useremail==data.email or useremail==data.username):
            if(passwd==data.password):
                if(data.active == 0 and data.verify_link==""):
                    link=make_password(random_string())
                    confirm_link=link.replace("+","")
                    verify_link="127.0.0.1:8000/verify/?link="+confirm_link
                    update=RoleDetails(email=data.email,verify_link=confirm_link)
                    update.save(update_fields=["verify_link"])
                    link_sending(data.email,data.username,verify_link)
                    return render(request,"sign_in.html",{"link": True})
                elif (data.active == 0 and data.verify_link != ""):
                    return render(request, "sign_in.html", {"verify": True})
                elif(data.active == 1):
                    request.session["authentication"]=True
                    request.session["email"]=data.email
                    update=RoleDetails(email=data.email, last_login=dt.datetime.now())
                    update.save(update_fields=["last_login"])
                    return render(request, "adminpanel.html")


    return render(request,"sign_in.html")

def verify(request):
    get_link=request.GET["link"]
    data=RoleDetails.objects.get(verify_link=get_link)
    if(get_link == data.verify_link):
        update=RoleDetails(email=data.email, active=1, verify_link="")
        update.save(update_fields=["active","verify_link"])
        return redirect("/sign_in/")

def sign_out(request):
    request.session["authentication"] = False
    request.session["email"] = ""
    return redirect("/sign_in/")

def homepage(request):
    return render(request, "homepage.html")

def index(request):
    return render(request, "adminpanel.html")

"""def sign_in(request):
    pas=request.POST["password"]
    data=RoleDetails.objects.get(email=request.POST["email"])
    passwd=data.password
    act=data.active
    if(act == 0):


    return render(request, "signin.html")"""

def sign_up(request):
    if(request.method=="POST"):

        form1 = RoleDetails(request.POST)  # create the object of the class
        if form1.is_valid():
            f2 = form1.save(commit=False)  # by default commit is true
            f2.usename = request.POST["username"]
            f2.fullname = request.POST["fullname"]  # data comes here from input text
            f2.mobileno = request.POST["mobileno"]
            f2.email = request.POST["email"]
            f2.password = request.POST["password"]
            f2.confirm_password = request.POST["confirm_password"]
            f2.gender = request.POST["gender"]
            f2.address = request.POST["address"]
            #f2.verify_link=
            #f2.active = 0
            f2.save()
            return render(request, "sign_up.html",{'success': True})
        else:
            return render(request, "sign_up.html",{'failed': True})
    return render(request, "sign_up.html")

def testimonial(request):
    return render(request, "about.html")



