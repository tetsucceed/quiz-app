from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Quiz

def index(request):
	latest_quiz_list = Quiz.objects.order_by('id')[:5]
	template = loader.get_template('quiz_view/index.html')
	context = {
		'latest_quiz_list':latest_quiz_list,
	}
	#output = ', '.join([q.title for q in latest_quiz_list])
	return HttpResponse(template.render(context, request))

def quiz(request, quiz_id):
	return HttpResponse("Quiz is %s" % quiz_id)

def result(request, quiz_id):
	return HttpResponse("Result of quiz %s" % quiz_id)

# Create your views here.
