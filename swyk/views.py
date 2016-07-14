from django.shortcuts import render

def ajax(request,offset):
	return render(request,offset)

def test(request):
    return render(request,"ccb7381c767a.html")

def home(request):
	return render(request,"comingSoon.html")

def dnswl(request):
	return render(request,"dnswl.txt")
	
def cert(request):
	return render(request,"qfr4BFxqSe0ipudatp5a-8fSFQ6Qoid6ZBkvEcCJKCk")
