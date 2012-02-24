from django.db import models

# Create your models here.

class Question(models.Model) :
		question_text = models.TextField() # place to add question text

		# all classes need a __unicode__ method defined 

		def __unicode__(self):
				return self.question_text

class Answer(models.Model) :
		question = models.ForeignKey('Question') # make a foriegn key relationship with Question - 1 Q can have many Answers.
		answer_text = models.TextField() # place to add answer text

		def __unicode__(self):
				return self.answer_text


