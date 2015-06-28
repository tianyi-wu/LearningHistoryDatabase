from django.contrib import admin
from analyze.models import Score

# Register your models here.
class ScoreAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'a', 'b', 'c', 'd', 'e')
	list_filter = ('user_profile__grade', 'user_profile__department',)
	change_list_template = "admin/analyze_change_list.html"

admin.site.register(Score, ScoreAdmin)
