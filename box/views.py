# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from models import Question
from models import Answer
from models import LoginForm
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from django import forms
from django.shortcuts import render_to_response

# The views are callbacks [ functions which are hooked to urls.py ]
# When a particular url pattern is matched , the parameters are passed onto 
# the view. Here we have only two views - the first one is callback for default
# url, and accepts no extra parameters [ all views have to take atleast one parameter ]
# the second view is hooked to the url of type ' http://urlname/question/8 '
# it displays the answer(s) for the 8th question, then. The num parameter transfers the 
# number to the function


def list_questions(request) :
		## list all the questions

		obj = Question.objects.all()

		if request.user.is_authenticated() :
			auth = True
		else :
			auth = False
		
		t = loader.get_template('qbox/index.html')
		c = Context({ 
			'obj' : obj,
			'auth' : auth,
					 
		})

		return HttpResponse(t.render(c))


def list_answers(request, num) :

		foo = Answer.objects.all().filter(question = num) # find the answers for the given question
		bar = Question.objects.all().filter(id = num)	
		
		if request.user_is_authenticated() :
			auth = True
		else :
			auth = False
			
		t = loader.get_template('qbox/answer.html')
		c = Context({ 
			'foo' : foo , 
			'bar' : bar ,
			'auth' : auth, 
		})

		return HttpResponse(t.render(c))

# Finally, define a view for the login

def login(request) :
		def errorHandle(error) :   
		
		# define a local errorhandler - notice how its defined inside another function to reduce scope
		# basically, all it does is, if an error is detected, the errorhandle is invoked
		# and it returns an errortype along with a loginform
			
			form = LoginForm()
			return render_to_response('qbox/login.html', {
					'error' : error, 
					'form' : form,
			})
		
		if request.method == 'POST' : # We don't want to listen to GET
			form = LoginForm(request.POST)
			
			if form.is_valid() : # performs various validity checks by django
				uname = request.POST['username']
				passw = request.POST['password']
				
				user = authenticate(uname = username, passw = password)
				
				if user is not None : # If valid user, then
					if user.is_active : # a boolean flag set to indicate that user hasn't deactivated their account
						
						# Go back to main page - indicate that the user has logged in successfully
						login(request, user)
						return list_questions(request)
					else :
						# Account is dead - inform the user
						error = u'Dang, this account has been suspended - contact the admins' # the u prefix is for unicode, btw
						return errorHandle(error)
				else :
					error = u'Wrong username or password!'
					return errorHandle(error)
			else :
				error = u' Something nasty happened - hang on '
				return errorHandle(error)
		else :
			form = LoginForm()
			return render_to_response('qbox/login.html', {
					'form' : form
			})


