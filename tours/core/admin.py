from django.contrib import admin
from .models import Cliente, Transporte, Destino, Nacionalidad
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'email', 'inicio', 'fin', 'destino', 'nacionalidad', 'transporte')
    list_filter = ('destino','transporte')
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Transporte)
admin.site.register(Destino)
admin.site.register(Nacionalidad)