from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client
account_sid = "AC0c55f3a344f5c614dac9ac2ad6cc52ff"
auth_token = "9d8d9591b60d44b2583a5615347bc090"




from .models import Post,Post_form,otp_db
from .form import PostForm
import random


# Create your views here.

#
def otp_generator():
    return random.randrange(100, 99999, 1)
#



def park_create(request,id=None):
	sti=str(id)
	new=Post.objects.create(A1=sti[0],A2=sti[1],A3=sti[2],A4=sti[3])
	return park_list(request)



def park_list(request):
	queryset=Post.objects.all()
	context={
	   "object_list":queryset,
	   "title":"List"
	}
	return render(request,"park/table.html",context) 


def park_home(request):
	queryset=Post.objects.all()
	info=queryset[len(queryset)-1]
	for obj in queryset:
		time=str(obj.timestamp)
		time=time.split()
		time=time[1][0]+time[1][1]
		
	info=str(info.A1)+str(info.A2)+str(info.A3)+str(info.A4)
	context={
	   "title":info
	}
	return render(request,"park/index.html",context) 





def graphs(request):
	queryset=Post.objects.all()
	timeFrequency=[]
	for i in range(0,25):
		timeFrequency.append(0)
	for obj in queryset:
		time=str(obj.timestamp)
		time=time.split()
		time=time[1][0]+time[1][1]
		timeFrequency[int(time)]=timeFrequency[int(time)]+1
	#print timeFrequency

	#converting timeFrequency into string
	info=''
	for i in range(1,25):
		info=info+' '+str(timeFrequency[i])

	context={
	   "title":info
	}
	print info[0]
	return render(request,"park/graph.html",context)


def post_create(request):
	form=PostForm(request.POST or None)
        client = Client(account_sid, auth_token)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save() 
                otpi=str(otp_generator())
                otp_db.objects.create(otp=otpi)
                client.messages.create(
                     to="+91"+instance.Number,
                     from_="+12722000622",
                     body="you've parked ur otp is"+otpi)
                
	context={
	    "form":form,
	}
	return render(request,"park/form.html",context)



def user_list(request):
	queryset=Post_form.objects.all()
        otp_set=otp_db.objects.all()
	context={
           "otp_list":otp_set,
	   "object_list":queryset,
	   "title":"List"
	}
	return render(request,"park/table1.html",context) 
















