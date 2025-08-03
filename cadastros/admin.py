from django.contrib import admin
from .models import Cliente ,Produto, Venda


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Venda)