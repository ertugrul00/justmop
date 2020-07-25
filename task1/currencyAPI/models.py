from django.db import models

class DBModel(models.Model):
    saved_dict = models.CharField('Name', max_length=120)    
    time = models.CharField('Time', max_length=120)
