"""egr"""
from django.http import HttpResponse
from foods.models import Food
from django.template.loader import render_to_string

def home(request):

	name = "Kai"
	
	#burger = Food("")
	#	 Food.title
	obj = Food.objects.get(id=1)
	#    

	#Django template 

	my_list = [102, 12, 45, 34, 34]
	#food_qs =  Food.objects.all() QuerySet ex .filter()
	context = {
		"my_list": my_list,
		"obj": obj,
		"name": obj.name,
		"carbs": obj.carbs,
		"saturated_fat": obj.saturated_fat
	}
	HTML_STRING = render_to_string("home.html",
		context=context)
	#HTML_STRING = f"""<h1>Hi {name}, 
	#Welcome to the Home Page</h1>"""

	"""
	Take in a request from django
	and return HTML
	"""
	return HttpResponse(HTML_STRING)