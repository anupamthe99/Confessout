from email import message
from django.shortcuts import render
from Confession.models import Confession
from Confession.models import Contact
# Create your views here.
def index(request):
    disctionary={"activehome":"active"}
    print("Hello")
    return render(request,"index.html",disctionary)
def confession(request):
    if request.method=="POST":
        print("hey whats up man")
        message=request.POST.get('confession-msg')
        print(message)
        ins=Confession(message=message)
        ins.save()
        print("The data has been written")
    disctionary={"message":message,"activehome":"active"}  
    return render(request,"confession.html",disctionary)
def colleges(request):
    disctionary={"activecolleges":"active"}
    return render(request,"colleges.html",disctionary)
def Contactt(request):
    
    disctionary={"activecontact":"active"}
    if request.method=="POST":
        messagee=True
        disctionary["message"]=messagee
        print("Hey you how are you ?")
        name=request.POST.get('name')
        print(name)
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,subject=subject,email=email,message=message)
        contact.save()
        return render(request,"contact.html",disctionary)
    return render(request,"contact.html",disctionary)
def about(request):
    disctionary={"activeabout":"active"}
    return render(request,"about.html",disctionary)
