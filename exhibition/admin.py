from django.contrib import admin
from .models import Painting
from .models import Artist

class PaintingModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'image', 'year', 'author', 'genre']
	list_display_links = list_display
	
	class Meta:
		model = Painting
	
class ArtistModelAdmin(admin.ModelAdmin):
	list_display = ['last_name']	

	class Meta:
		model = Artist

# Register your models here.
admin.site.register(Painting, PaintingModelAdmin)
admin.site.register(Artist, ArtistModelAdmin)


