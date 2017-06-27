from django.db import models

class GrammarCard(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	comment = models.TextField()
	category = models.CharField(max_length=64, default="grammar")

	def __str__(self):
		return self.title + ": " + self.body  + ", " + self.comment + ", " + self.category

class Koyla(models.Model):
	word = models.CharField(max_length=30)
	la = models.CharField(max_length=30)
	comment = models.CharField(max_length=100)
	grammarCard = models.ForeignKey(GrammarCard, blank=True, null=True)

	def __str__(self):
		return self.word + " == " + self.la + ", comment: " + self.comment

class Card(models.Model):
	front = models.CharField(max_length=100)
	back = models.CharField(max_length=100)
	flip = models.BooleanField()
	grammarCard = models.ForeignKey(GrammarCard, blank=True, null=True)

	def __str__(self):
		return self.front + " == " + self.back

class Intro(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()