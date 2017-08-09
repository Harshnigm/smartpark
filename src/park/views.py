from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.




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




