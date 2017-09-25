from django.contrib import admin

from .models import * 

class QuestionsInline(admin.StackedInline):
	model = Questions
	extra = 3


class QuizAdmin(admin.ModelAdmin):
	fields = ['title']
	inlines = [QuestionsInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions)
admin.site.register(Answers)

# Register your models here.
