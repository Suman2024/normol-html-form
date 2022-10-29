from django.shortcuts import render
from django.http import HttpResponse

from app.models import *
# Create your views here.
def htmlform(request):
    if request.method=='POST':
        n=request.POST['un']
        p=request.POST['pw']
        d={'n':n,'p':p}
        return render(request,'data.html',d)
    return render(request,'htmlform.html')

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('topic is insert successfull go and check admin')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        tn=request.POST.get('topic')
        n=request.POST.get('name')
        u=request.POST.get('url')
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
        W.save()
        return HttpResponse('web page is insertion is succefully if you want to see check in admib')
    return render(request,'insert_webpage.html',d) 

def select_topic(request):
    topics = Topic.objects.all()
    d = {'topics': topics}
    if request.method == 'POST':
        tn = request.POST.getlist('topic')
        print(tn)
        webpages = Webpage.objects.none()
        for i in tn:
            webpages = webpages | Webpage.objects.filter(topic_name=i)
        d1 = {'webpages': webpages}
        return render(request, 'display_webpage.html', d1)
    return render(request, 'select_topic.html', d)


def check_box(request):
    T=Topic.objects.all()
    d={'topics':T}
    return render(request,'check_box.html',d)

def radio(request):
    T=Topic.objects.all()
    d={'topics':T}
    return render(request,'radio.html',d)

 