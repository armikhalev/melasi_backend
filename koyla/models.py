from django.db import models

class Koyla(models.Model):
	word = models.CharField(max_length=30)
	la = models.CharField(max_length=30)
	comment = models.CharField(max_length=100)

	def __str__(self):
		return self.word + " == " + self.la + ", comment: " + self.comment
