from django.db import models

# Create your models here.


class Question(models.Model):

    question = models.CharField(max_length=200)


class Interview(models.Model):

    name = models.CharField(max_length=50, unique=True)
    start_time = models.DateTimeField(editable=False)
    finish_time = models.DateTimeField()
    description = models.CharField()
    questions = models.ManyToManyField(to=Question)

