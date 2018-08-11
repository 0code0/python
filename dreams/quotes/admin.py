from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class authorAdmin(admin.ModelAdmin):
	list_display = ('name','user','submitedon','isapproved')

admin.site.register(author,authorAdmin)

class categoryAdmin(admin.ModelAdmin):
	list_display = ('name','user','submitedon','isapproved','isdeleted')

admin.site.register(category,categoryAdmin)

class quotesAdmin(admin.ModelAdmin):
	list_display = ('quotes','user','author','submitedon','isapproved')

admin.site.register(quotes,quotesAdmin)

