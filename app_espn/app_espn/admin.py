from django.contrib import admin
from .models import Kategori, UserWartawan, UserNetijen, Artikel, Komen, Like

# Register your models here.
admin.site.register(Kategori)
admin.site.register(UserWartawan)
admin.site.register(UserNetijen)
admin.site.register(Artikel)
admin.site.register(Komen)
admin.site.register(Like)