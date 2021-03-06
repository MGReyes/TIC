from django.contrib import admin
from formulario.models import Form

class FormAdmin(admin.ModelAdmin):
    fields = ['Nombre', 'Apellido']
    list_display = ('Nombre', 'Apellido')
    list_filter = ['Apellido', 'Nombre']
    search_fields = ['Nombre', 'Apellido']
#     date_hierarchy = '' ordenar por fecha

admin.site.register(Form, FormAdmin)
    
