from django.contrib import admin
from .models import Line
from .models import Background

def make_active(modeladmin, request, queryset):
    queryset.update(status=True)
make_active.short_description = 'Mark selected as active'

def make_inactive(modeladmin, request, queryset):
    queryset.update(status=False)
make_inactive.short_description = 'Mark selected as inactive'

class LineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'status')
    list_filter = ['status']
    search_fields = ['title', 'image']
    actions = [make_active, make_inactive]
    list_editable = ['title', 'image', 'status']

class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('image', 'status')
    list_filter = ['status']
    search_fields = ['image']
    actions = [make_active, make_inactive]
    list_editable = ['status']

admin.site.register(Line, LineAdmin)
admin.site.register(Background, BackgroundAdmin)
