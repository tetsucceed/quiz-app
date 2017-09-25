from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'(?P<quiz_id>[0-9]+)/quiz/$', views.quiz, name='quiz'),
	url(r'(?P<quiz_id>[0-9]+)/quiz/result/$', views.result, name='results'),
	]
