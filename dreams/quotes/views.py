from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from . import forms
from quotes.models import *

def index(request):

	context = {"quotes":quotes.objects.filter(isapproved=True).filter(isdeleted=False)}
	return render(request,"index.html",context)

def about(request):
	return render(request,"about.html")

def author(request,authorname):
	authquo = quotes.objects.filter(author__name=authorname)
	if not authquo:
		if request.user.is_authenticated:
			return render(request,"usererror.html",{"authorname":authorname})
		else:
			return render(request,"error.html",{"authorname":authorname})
				
	else:	
		context = {"author_quotes":authquo,"authorname":authorname}
		return render(request,"author.html",context)

def categoryname(request,categoryname):
	
	quo = quotes.objects.filter(category__name=categoryname)
	if not quo:
		if request.user.is_authenticated:
			return render(request,"usererror.html",{"categoryname":categoryname})
		else:	
			return render(request,"error.html",{"categoryname":categoryname})
	else:	
		context = {"category_quotes":quo,"categoryname":categoryname}
		return render(request,"categoryname.html",context)



def registration(request):
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = authenticate(username=username,password=password)
			login(request,user)
			return HttpResponseRedirect("/")	
	else:
		form = forms.SignUpForm()
		
	context = {'form':form}
	return render(request,"registration.html",context)

def profile_view(request):
	return render(request,"user/profile.html")	

def updatevalue(request):
	temp = ""
	if request.GET:
		value = request.GET["data"].split("_")
		quo = quotes.objects.get(id=value[1])
		if value[0] == "shareFacebook":
			quo.shareFacebook = quo.shareFacebook + 1
			quo.save()
			temp = "facebook"

		elif value[0] == "shareWhatsapp":
			quo.shareWhatsapp = quo.shareWhatsapp + 1
			quo.save()
			temp = "whatsapp"

		elif value[0] == "shareInstagram":
			quo.shareInstagram = quo.shareInstagram + 1
			quo.save()
			temp = "instagram"

		else :
			quo.copyquotes = quo.copyquotes + 1
			quo.save()	
			temp = "copy"	
	

	return HttpResponse(temp)	


def searchquotes(request):
	if request.GET:
		try:
			quote = quotes.objects.get(id=request.GET["id"])	
			context = {"quote":quote}
			return render(request,"searchquotes.html",context)
			
		except Exception as e:
			return render(request,"error.html",{"id":request.GET["id"]})
	else:
		return HttpResponseRedirect("/")	
