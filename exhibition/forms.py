from django import forms
from .models import Painting

class PaintingForm(forms.ModelForm):
	model = forms.Form
#	fields = ['title', 'content', 'genre', 'post_author']
	
	class Meta:
		model = Painting
		fields = ['title', 'year', 'genre', 'author', 'image']
