from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=23, null=True)
    section = models.ForeignKey("Section", on_delete=models.CASCADE)
    age = models.IntegerField()
    phone = models.CharField(max_length=34, null=True)
    address = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.name}, {self.user}'
    
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_field = models.CharField(null=True, max_length=2000)
    section = models.ForeignKey("Section", on_delete=models.CASCADE)
    
    
class Section(models.Model):
    section = models.CharField(max_length=255, null=True)

class Grade(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_field = models.CharField(null=True, max_length=35)
    
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_field = models.CharField(max_length=2000, null=True)
