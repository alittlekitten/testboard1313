from django.db import models

# Create your models here.
class Board(models.Model): # 변수와 함수의 집합
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title