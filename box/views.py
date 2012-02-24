# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from models import Question
from models import Answer
from django.template import Context, loader

# The views are callbacks [ functions which are hooked to urls.py ]
# When a particular url pattern is matched , the parameters are passed onto 
# the view. Here we have only two views - the first one is callback for default
# url, and accepts no extra parameters [ all views have to take atleast one parameter ]
# the second view is hooked to the url of type ' http://urlname/question/8 '
# it displays the answer(s) for the 8th question, then. The num parameter transfers the 
# number to the function


def listq(request) :
		## list all the questions

		obj = Question.objects.all()
		t = loader.get_template('qbox/index.html')
		c = Context({ 'obj': obj 
		})

		return HttpResponse(t.render(c))


def lista(request, num) :

		foo = Answer.objects.all().filter(question = num) # find the answers for the given question
		bar = Question.objects.all().filter(id = num)	
		t = loader.get_template('qbox/answer.html')
		c = Context({ 'foo': foo , 'bar': bar 
		})

		return HttpResponse(t.render(c))


