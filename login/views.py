from django.shortcuts import render_to_response,render

# Create your views here.

context = dict()

context["title"] = "Share What You Know - SWYK"

def home(request):
	return render_to_response("auth.html",context)

def login(request):
	post = 0
	try:
		if request.POST['submit']:
			post = 1
	except:
		pass

	if post:
		return render(request,"login.html",context)
	else:
		return render(request,"login.html",context)