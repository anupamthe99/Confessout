from email import message
from email.mime import image
import imp
from unittest import result
from django.shortcuts import render
from numpy import source
from Confession.models import Contact

# for text to img covert
from PIL import Image, ImageDraw, ImageFont
import textwrap

from random import random

# Create your views here.
def index(request):
    disctionary={"activehome":"active"}
    return render(request,"index.html",disctionary)
def confession(request):
    if request.method=="POST":
        message=request.POST.get('confession-msg')
        ide=random()
        print("=============================================================================")

        # Drawing image
        img = Image.new('RGB', (1080, 1080), color=(0, 0, 0))
        d1 = ImageDraw.Draw(img)

        myFont = ImageFont.truetype("arial.ttf", size=40)
        words = message
        lines = textwrap.wrap(words, width=60)
        a = 0
        for word in lines:
            d1.text((0, a), word, fill=(255, 255, 255), font=myFont)
            a += 40
        img.save(f"gallery/{ide}.jpeg")
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
