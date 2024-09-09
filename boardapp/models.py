from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to='')#どこに保存するのか指定する引数必要
    #settings.pyで保存先を指定する場合はこの形でOK
    good = models.IntegerField()
    read = models.IntegerField()#既読の数を数える
    readtext = models.TextField()#既読を押した人の情報を記録
    
    