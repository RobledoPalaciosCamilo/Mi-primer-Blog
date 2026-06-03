from django.contrib import admin
from .models import Post, Perfil
# Register your models here.

# Personalizamos la vista del Post en el administrador
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Definimos qué columnas queremos ver en la lista principal
    list_display = ('titulo', 'autor', 'fecha_creacion')
    
    # Agregamos una barra de búsqueda para buscar por título o asunto
    search_fields = ('titulo', 'asunto')
    
    # Agregamos filtros laterales por fecha o por autor
    list_filter = ('fecha_creacion', 'autor')

# Registramos el Perfil de forma simple
admin.site.register(Perfil)