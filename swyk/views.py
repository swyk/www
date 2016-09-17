from django.shortcuts import render
from comingSoon.models import *
from django.contrib.auth.decorators import login_required

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

		receivers = [request.POST['email']]

		allmails = Email.objects.all()

		for mail in allmails:
			send_mail(receivers,mail.id)

		context['message'] = 1
	return render(request,"comingSoon.html",context)

@login_required
def send_bulk_mail(request):
	return render(request,"comingSoon.html")

def send_mail(receivers,mailID):
	sender = 'team@swyk.cf'
	newMail = Email.objects.all().filter(id=mailID)[0]
	message= newMail.headers%(','.join(receivers))+"\nSubject: "+newMail.subject+"\n\n"+newMail.body
	smtpObj = smtplib.SMTP_SSL('smtp.yandex.com')
	smtpObj.login("team@swyk.cf","DYKWIA@bcf184")
	smtpObj.sendmail(sender,receivers,message)
	newMail = 0