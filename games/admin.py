from django.contrib import admin
from .models import *


class GamesAdmin(admin.ModelAdmin):
    list_display = ('title' ,'console' , 'category','price' ,
                    'os' , 'cpu' , 'gpu' , 'ram' , 'hdd',
                    'shortDescription' ,
                    'longDescription' , 'coverImg' ,
                    'img1Url' , 'img2Url' ,'img3Url',
                    'youtubeUrl')

admin.site.register(Games,GamesAdmin)