from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Painting, Artist

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import context
from .forms import PaintingForm


# Create your views here.
def paintingDetails(request, id=None):
	instance = get_object_or_404(Painting,id=id)
	context = {'title':'Post Detail', 'instance': instance}
	return render(request, 'painting_details.html', context)
	
def paintingModifying(request, id = None):
	instance = get_object_or_404(Painting, id=id)
	form = PaintingForm(request.POST or None, instance = instance)
	
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		
	context = {
			'pageFunction': 'Update', 
			'title': instance.title,
			'instance': instance,
			'form': form
	}
	return render(request, 'painting_adding.html', context)

#def post_delete(request):
#	return HttpResponse('<h4> ma header </h4>')
#	
def paintingAdding(request):
	form = PaintingForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	
	context = {
		'pageFunction': 'Add', 
		'form':form
	}
	
	return render(request, 'painting_adding.html', context)
	
def paintingsList(request):
	paintingsSet = Painting.objects.all()
	context = {'paintingsSet':paintingsSet, 'title': 'Paintings List'}
	return render(request, 'index.html', context)
