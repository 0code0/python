from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from quotes.models import *
import datetime

def profile_view(request):
	if request.user.is_authenticated:
		
		quotesdatas = quotes.objects.filter(user=request.user)
		data = quotesdatas.aggregate(copyquotes_sum = Sum('copyquotes'),shareFacebook_sum = Sum("shareFacebook"),shareWhatsapp_sum =Sum("shareWhatsapp"),shareInstagram_sum =Sum("shareInstagram"))
	 
		context = {"quotesdatas":quotesdatas,"data":data}

		return render(request,"user/profile.html",context)
	else:
		return HttpResponseRedirect("/accounts/login/")	

@csrf_exempt
def qcategory(request):

	if request.method =='POST':
		categoryname = request.POST["Category"]
		cat_o = category(name=categoryname,user=request.user)
		cat_o.save()
		get_all_category_by_user = category.objects.filter(user=request.user).filter(isdeleted=False)
		context = {"get_all_category_by_user":get_all_category_by_user}

		return render(request,"user/ManageQuotesCategory.html",context)	

	if request.GET.get("delete"):
		category.objects.filter(id=request.GET.get("delete")).update(isdeleted=True)

	get_all_category_by_user = category.objects.filter(user=request.user).filter(isdeleted=False)
	context = {"get_all_category_by_user":get_all_category_by_user}
	return render(request,"user/ManageQuotesCategory.html",context)

def qauthor(request):
	if request.method =='POST':
		authorname = request.POST["author"]
		auth_o = author(name=authorname,user=request.user)
		auth_o.save()
		get_all_author_by_user = author.objects.filter(user=request.user).filter(isdeleted=False)
		context = {"get_all_author_by_user":get_all_author_by_user}

		return render(request,"user/ManageAuthor.html",context)	

	if request.GET.get("delete"):
		author.objects.filter(id=request.GET.get("delete")).update(isdeleted=True)
				
	get_all_author_by_user = author.objects.filter(user=request.user).filter(isdeleted=False)
	context = {"get_all_author_by_user":get_all_author_by_user}
	return render(request,"user/ManageAuthor.html",context)	

def qquotes(request):

	if request.method =='POST':
		categories = category.objects.filter(user=request.user).filter(isdeleted=False)
		authors = author.objects.filter(user=request.user).filter(isdeleted=False)
		authorid = request.POST["authorid"]
		categoryid = request.POST["categoryid"]
		quote = request.POST["quotes"]
		if quote.startswith('"') and quote.endswith('"'):
			quote = quote[1:]
			quote = quote[:-1]
		if request.user.is_staff:
			quotes_o = quotes(quotes=quote,author=author.objects.get(id=authorid),category=category.objects.get(id=categoryid),user=request.user,isapproved=True)
		else:		
			quotes_o = quotes(quotes=quote,author=author.objects.get(id=authorid),category=category.objects.get(id=categoryid),user=request.user)
		quotes_o.save()
		get_all_quotes_by_user = quotes.objects.filter(user=request.user).filter(isdeleted=False)
		context = {"get_all_quotes_by_user":get_all_quotes_by_user,'categories':categories,'authors':authors}

		return render(request,"user/ManageQuotes.html",context)	

	if request.GET.get("delete"):
		quotes.objects.filter(id=request.GET.get("delete")).update(isdeleted=True)
				
	get_all_quotes_by_user = quotes.objects.filter(user=request.user).filter(isdeleted=False)
	categories = category.objects.filter(isdeleted=False)
	authors = author.objects.filter(isdeleted=False)
	context = {"get_all_quotes_by_user":get_all_quotes_by_user,'categories':categories,'authors':authors}
	return render(request,"user/ManageQuotes.html",context)	