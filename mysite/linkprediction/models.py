from django.db import models

import datetime 
from django.utils import timezone
import random
# Create your models here.
# A model is the single, definitive source of truth about your data
# In our simple poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. 
# A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

class Tag(models.Model):
    tag_name = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Occupation(models.Model):
    id = models.IntegerField(primary_key=True,default=1)
    discription = models.CharField(max_length=20,verbose_name='职业')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = '职业'
        verbose_name_plural = verbose_name

# - Age is chosen from the following ranges:
# 	*  1:  "Under 18"
# 	* 18:  "18-24"
# 	* 25:  "25-34"
# 	* 35:  "35-44"
# 	* 45:  "45-49"
# 	* 50:  "50-55"
# 	* 56:  "56+"
class Range(models.Model):
    age = models.PositiveIntegerField(verbose_name='年龄')
    description = models.CharField(max_length=10,verbose_name='年龄区间')

    def __str__(self):
        return str(self.age)

    class Meta:
        verbose_name = '年龄'
        verbose_name_plural = verbose_name

class Movie(models.Model):
    name = models.CharField(max_length=20,verbose_name='电影名')
    mid = models.CharField(max_length=10, verbose_name="电影序号")
    tags = models.ForeignKey(Tag,verbose_name="电影类别",null=True,on_delete=models.SET_NULL)
    abstract = models.TextField(blank=True,null=True,verbose_name="简介",default="这个电影还没有简介~")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name

class User(models.Model):
    name = models.CharField(max_length=128, verbose_name='姓名')
    password = models.CharField(max_length=256,verbose_name='密码')
    gender = (('male','男'),('female','女'))
    sex = models.CharField(max_length=4,verbose_name="性别",choices=gender)
    ageRange = models.ForeignKey(Range,verbose_name="年龄区间",null=True,on_delete=models.SET_NULL)
    occupation = models.ForeignKey(Occupation,verbose_name="职业",null=True,on_delete=models.SET_NULL)

    movies = models.ManyToManyField(Movie,through='Rating',verbose_name='看过的电影')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Rating(models.Model):
    user = models.ForeignKey(User,verbose_name='用户',null=True,on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie,verbose_name='电影',null=True,on_delete=models.SET_NULL)
    rating = models.PositiveIntegerField(verbose_name='评分')

    class Meta:
        verbose_name = '评分'
        verbose_name_plural = verbose_name




