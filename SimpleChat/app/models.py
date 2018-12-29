from django.db import models
from django.core import validators

# Create your models here.
class Users(models.Model):
    INSITE_STATE = (
        (1,'入室中'),
        (2,'退室'),
        )

    id = models.IntegerField(
        verbose_name='ユーザーＩＤ',
        validators=[validators.MinValueValidator(1)],
        primary_key = True,
        default = ''
    )

    name = models.CharField(
        verbose_name = '名前',
        max_length = 20,
        default = '',
    )

    isInsite = models.IntegerField(
        verbose_name = '入室状態',
        choices = INSITE_STATE,
        default = 2,
        )

class Talk(models.Model):
        id = models.IntegerField(
        verbose_name='発言ＩＤ',
        primary_key = True,
        default = '',
        )

        talk_text = models.CharField(
            verbose_name = '発言',
            max_length = 200,
            default = '',
            )

        user_id = models.ForeignKey(Users,on_delete=models.SET_DEFAULT,default=0)

        talk_datetime = models.DateField('発言日時')

class Chat_Log(models.Model):

        log_id = models.IntegerField(
        verbose_name='ログＩＤ',
        primary_key = True,
        )

        talk_id = models.ForeignKey(Talk,on_delete=models.SET_DEFAULT,default=0)

        talk_text = models.CharField(
            verbose_name = '発言',
            max_length = 200,
            )

        user_id = models.ForeignKey(Users,on_delete=models.SET_DEFAULT,default=0)

        talk_datetime = models.DateField('発言日時')