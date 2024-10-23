from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to='', null=True, blank=True)#どこに保存するのか指定する引数必要
    #settings.pyで保存先を指定する場合はこの形でOK
    good = models.IntegerField(default=0)
    good_users = models.ManyToManyField(User, related_name='good_posts', blank=True)# これで「Good」を押したユーザーを記録します
    read = models.IntegerField(null=True, blank=True, default=1)#既読の数を数える
    readtext = models.TextField(null=True, blank=True, default='a')#既読を押した人の情報を記録
    
class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()