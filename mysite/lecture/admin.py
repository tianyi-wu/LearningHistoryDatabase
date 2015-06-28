from django.contrib import admin

# Register your models here.
from lecture.models import Lecture, Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id','course_name','a','b','c','d','e','weight')
    search_fields = ['course_name']


class LectureAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['Lecture_id','Lecture_name']}),
    #    ('Date information', {'fields': ['Term']}),
    #]
    #inlines
    
    list_display = ('lecture_id','lecture_name','term')
    list_filter = ['term']
    search_fields = ['lecture_name']

admin.site.register(Lecture, LectureAdmin)
admin.site.register(Course, CourseAdmin)