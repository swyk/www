from django.shortcuts import render

def ajax(request,offset):
	return render(request,offset)

def test(request):
    return render(request,"ccb7381c767a.html")
