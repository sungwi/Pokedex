from email.policy import default
from django.db import models

class Pokemon(models.Model):
    name_en = models.CharField(max_length=100) # 英名
    name_ja = models.CharField(max_length=100) # 日名
    id_number = models.IntegerField()
    image_url = models.URLField()
    type = models.JSONField()
    genus = models.CharField(max_length=100, default='unknown') # 分類
    text = models.TextField(default=None)
    ability = models.JSONField(default=dict)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)