from django.contrib import admin
from .models import Profile, Conta, Receita

# Register your models here.

admin.site.register(Profile)
admin.site.register(Conta)
admin.site.register(Receita)