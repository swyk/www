from django.shortcuts import render
from comingSoon.models import *

import smtplib

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
		sender = 'team@swyk.cf'
		receivers = [request.POST['email']]
		
		message = "From: Team SWYK <team@swyk.cf>\
			To: "+request.POST['email']+"\
			Subject: SWYK Subscription\
			Hi there,\
			Thank you for subscribing to SWYK, you will receive latest updates for the website SWYK.cf .\
			Thank you,\
			SWYK Team."
		
		try:
		   smtpObj = smtplib.SMTP('smtp.yandex.com')
		   smtpObj.sendmail(sender, receivers, message)         
		except smtplib.SMTPException:
		   print "Error: unable to send email"
		context['message'] = 1
	return render(request,"comingSoon.html",context)
