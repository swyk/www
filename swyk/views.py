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
		
		message = """From: SWYK Team <team@swyk.cf>\nTo: %s\nReply-To: no-reply@swyk.cf\nMIME-Version: 1.0\nContent-type: text/html\nSubject: Share What You Know Subscription\n\n
			
			Hi there,<br/>
			Thank you for subscribing to <i><b>Share What You Know</b></i>, you will be the first to know about
			any updates for the website.<br/><br/>
			
			If you didn't regester for SWYK, you can unsubscribe through our next email.<br/><br/>
			
			Best,<br/>
			SWYK Team.<br/>
			"""%(",".join(receivers))
		smtpObj = smtplib.SMTP_SSL('smtp.yandex.com')
		smtpObj.login("team@swyk.cf","DYKWIA@bcf184")
		smtpObj.sendmail(sender, receivers, message)
		
		context['message'] = 1
	return render(request,"comingSoon.html",context)
