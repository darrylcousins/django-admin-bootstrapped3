from django.contrib import admin
from .models import CapitalModel

class CaptialModelAdmin(admin.ModelAdmin):
    model = CapitalModel
    list_display = ['name']
    search_fields = ['name', ]
    list_editable = ['name', ]
    list_filter = ['name']
    list_per_page = 3
    save_as = True
    save_on_top = True

# Register your models here.
admin.site.register(CapitalModel, CaptialModelAdmin)
