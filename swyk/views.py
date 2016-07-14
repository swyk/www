from django.shortcuts import render

def ajax(request,offset):
	return render(request,offset)

def home(request):
	return render(request,"comingSoon.html")

