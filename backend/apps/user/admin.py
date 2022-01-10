from django.contrib import admin

# Register your models here.
from .models import PreferOttContentGenre, User

admin.site.register(User)
admin.site.register(PreferOttContentGenre)
