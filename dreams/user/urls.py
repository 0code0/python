from django.urls import path

from . import views
urlpatterns = [
	path('profile/', views.profile_view, name='profile_view'),
	path('qcategory/', views.qcategory, name='qcategory'),
	path('author/', views.qauthor, name='qauthor'),
	path('quotes/', views.qquotes, name='qquotes'),


]