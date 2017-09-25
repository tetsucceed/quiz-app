from django.db import models

class Quiz(models.Model):
	title = models.CharField(max_length=255, unique=True)
#	questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class Questions(models.Model):
    question_text = models.CharField(max_length=255, unique=True)
    quizes =  models.ForeignKey(Quiz, on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text

class Answers(models.Model):
    answer_text = models.CharField(max_length=255, unique=True)
    weight = models.IntegerField(default=0)
    choice_int = models.IntegerField(default=0)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer_text
    def answer_weight(self):
        return self.weight


# Create your models here.
