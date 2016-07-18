from django.shortcuts import render
from comingSoon.models import *
def ajax(request,offset):
	return render(request,offset)

def home(request):
	context = {
		'message' : 0,
		'already_registered' : 0,
	}
	if request.POST:
		subscribers = Subscriber.objects.all().filter(email = request.POST['email'])
		if len(subscribers) > 0:
			context['already_registered'] = 1
			return render(request,"comingSoon.html",context)
		newSubscriber = Subscriber()
		newSubscriber.email = request.POST['email']
		newSubscriber.save()
		context['message'] = 1
	return render(request,"comingSoon.html",context)
