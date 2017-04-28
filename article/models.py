# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length = 100)    #blog theme
	category = models.CharField(max_length = 50,blank = True) #blog remark
	date_time = models.DateTimeField(auto_now_add = True)  #blog time
	content = models.TextField(blank = True,null = True) #blog text
	

	#python2 use  "__unicode__",python3 use "__str__"
	def __unicode__(self):
		return self.title
	
	#decline by time
	class Meta:
		ordering = ['-date_time']
