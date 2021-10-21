from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


class BoardModel(models.Model):
    class Category(models.TextChoices):
        JPOP = 'J-POP', _('J-POP')
        KPOP = 'K-POP', _('K-POP')
        ANISON = 'ANISON', _('ANISON')
        ROCK = 'ROCK', _('ROCK')
        JAZZ = 'JAZZ', _('JAZZ')
    
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=12, choices=Category.choices)
    song = models.CharField(max_length=64)
    artist = models.CharField(max_length=64)
    music = models.URLField()
    subtitle = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'board'
        
    # 投稿フォームでboardの表示をわかりやすくするためのもの
    def __str__(self):
        return self.song
        
class PosterModel(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, to_field='username' ,on_delete=CASCADE)
    board = models.ForeignKey('BoardModel', to_field='id', on_delete=CASCADE)
    content = models.CharField(max_length=2048)
    posted_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'poster'