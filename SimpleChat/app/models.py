from django.db import models
from django.core.validators import RegexValidator, slug_re
from django.utils import timezone
# Create your models here.


class Users(models.Model):
    INSITE_STATE = (
        (1,'入室中'),
        (2,'退室'),
        )

        
    id = models.CharField(
        verbose_name = 'ユーザーID',
        max_length = 10,
        primary_key = True,
        validators=[RegexValidator(
        slug_re,
        '名前には半角英数字、アンダーバー、ハイフンのみ指定できます。',
        'invalid')]
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
        talk_text = models.TextField(
            verbose_name = '発言',
            max_length = 200,
            default = '',
            )

        user_id = models.ForeignKey(Users,on_delete=models.SET_DEFAULT
                                         ,default='')

        talk_datetime = models.DateTimeField(verbose_name='発言日時'
                                           , default=timezone.now)

class Chat_Log(models.Model):
        talk_id = models.ForeignKey(Talk,on_delete=models.SET_DEFAULT,default=0)

        talk_text = models.TextField(
            verbose_name = '発言',
            max_length = 200,
            )

        user_id = models.ForeignKey(Users,on_delete=models.SET_DEFAULT
                                         ,default='')

        talk_datetime = models.DateTimeField('発言日時')