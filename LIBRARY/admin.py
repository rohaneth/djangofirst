from django.contrib import admin

from .models import books,movies


class booksAdmin(admin.ModelAdmin):


    list_display  = ['book_name','subject']

admin.site.register(books,booksAdmin)

# Register your models here.

class moviesAdmin(admin.ModelAdmin):
    list_display=['movie_name','subject']

admin.site.register(movies,moviesAdmin)