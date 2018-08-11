from django.urls import path

from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('author/<authorname>', views.author, name='author'),
	path('category/<categoryname>', views.categoryname, name='categoryname'),
	path('registration/', views.registration, name='registration'),
	path('profile/', views.profile_view, name='profile_view'),
	path('updatevalue/', views.updatevalue, name='updatevalue'),
	path('search/', views.searchquotes, name='searchquotes'),

	

]