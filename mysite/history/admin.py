from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers

# Register your models here.
from history.models import History

def analyze(modeladmin, request, queryset):
    response = HttpResponse(content_type = "application/json")
    serializers.serialize("json", queryset,stream=response)
    return response
analyze.short_description = "Analyze"

class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['lecture','student']}),
        ('Date information', {'fields': ['year','term']}),
        ('Grade information', {'fields': ['grade']}),
    ]
    #inlines
    
    list_display = ('lecture','student','year','grade')
    list_filter = ['student','lecture','year']
    search_fields = ['lecture']
    change_list_template = "admin/analyze_change_list.html"
    actions = [analyze]

admin.site.register(History, HistoryAdmin)
