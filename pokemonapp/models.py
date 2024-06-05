from django.db import models

class Pokemon(models.Model):
    name_en = models.CharField(max_length=100) # 英名
    name_ja = models.CharField(max_length=100) # 日名
    id_number = models.IntegerField()
    image_url = models.URLField()
