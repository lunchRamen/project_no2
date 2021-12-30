from django.contrib import admin

# Register your models here.
from .models import User,Prefer_ott_content_genre

admin.site.register(User)
admin.site.register(Prefer_ott_content_genre)
