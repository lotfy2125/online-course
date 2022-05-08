from random import choices
from django.contrib import admin
# <HINT> Import any new Models here
from .models import *

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class ChoiceInline(admin.TabularInline ):
    model = Choice
    extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text','is_correct']
    


class QuestionAdmin(admin.ModelAdmin):

    inlines = [ChoiceInline]
    list_display = ('course','Lesson','question_text','mark')





# <HINT> Register Question and Choice models here
admin.site.register(Submission)
admin.site.register(Question ,QuestionAdmin )
admin.site.register(Choice , ChoiceAdmin )
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
