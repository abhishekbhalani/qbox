from django.db import models
from django import forms 
# Create your models here.

class Question(models.Model) :
		question_text = models.TextField() # place to add question text
		#rating = #define rating here
		# all classes need a __unicode__ method defined 

		def __unicode__(self):
				return self.question_text

class Answer(models.Model) :
		question = models.ForeignKey('Question') # make a foriegn key relationship with Question - 1 Q can have many Answers.
		answer_text = models.TextField() # place to add answer text
		#rating = # define rating here

		def __unicode__(self):
				return self.answer_text

class LoginForm(forms.Form) :
		username = forms.CharField(max_length = 100)
		password = forms.CharField(widget=forms.PasswordInput(), max_length = 100)


