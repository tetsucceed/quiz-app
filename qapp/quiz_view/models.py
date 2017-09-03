from django.db import models


class Quiz(models.Model):
	title = models.CharField(max_length=255, unique=True)
	questions = models.ForeignKey('Questions', on_delete=models.CASCADE)

class Questions(models.Model):
	question_text = models.CharField(max_length=255, unique=True)
	answers =  models.ForeignKey('Answers', on_delete=models.CASCADE)

class Answers(models.Model):
	answer_text = models.CharField(max_length=255, unique=True)
	weight = models.IntegerField(default=0)
	choice_int = models.IntegerField(default=0)

# Create your models here.
