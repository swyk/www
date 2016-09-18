from django.shortcuts import render
from comingSoon.models import *
from django.contrib.auth.decorators import login_required
from random import randint

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
		alreadyUnSubscribed = UnSubscriber.objects.all().filter(email=request.POST['email'])
		if(len(alreadyUnSubscribed) > 0):
			bool(alreadyUnSubscribed)
			alreadyUnSubscribed[0].isUnsubscribed = False
			alreadyUnSubscribed[0].save()
		else:
			newUnsubscribed = UnSubscriber()
			newUnsubscribed.email = request.POST['email']
			newUnsubscribed.isUnsubscribed = False
			subCode = ''
			for _ in xrange(9):
				subCode += chr(randint(65,90))
			newUnsubscribed.subCode = subCode
			newUnsubscribed.save()
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
	UnSubscribera = UnSubscriber.objects.all().filter(email='.'.join(receivers))
	message= newMail.headers%(','.join(receivers))+"\nSubject: "+newMail.subject+"\n\n"+newMail.body%(','.join(receivers),UnSubscribera[0].subCode)
	print message
	smtpObj = smtplib.SMTP_SSL('smtp.yandex.com')
	smtpObj.login("team@swyk.cf","DYKWIA@bcf184")
	smtpObj.sendmail(sender,receivers,message)
	newMail = 0


def unsubscribe(request,offset):
	subEmail = request.GET.get("mail","")
	delSubscriber = Subscriber.objects.all().filter(email=subEmail)

	if(len(delSubscriber) > 0):
		message = 1
		alreadyUnSubscribed = UnSubscriber.objects.all().filter(email=subEmail)

		if alreadyUnSubscribed[0].subCode == request.GET.get("c",""):
			bool(alreadyUnSubscribed)
			alreadyUnSubscribed[0].isUnsubscribed = True
			delSubscriber[0].delete()
			alreadyUnSubscribed[0].save()
	else:
		message = 0 #error

	context = {
		"message":message
	}

	return render(request,"unSubscribe.html",context)