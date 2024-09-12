from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to='')#どこに保存するのか指定する引数必要
    #settings.pyで保存先を指定する場合はこの形でOK
    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)#既読の数を数える
    readtext = models.TextField(null=True, blank=True, default='a')#既読を押した人の情報を記録
    
    