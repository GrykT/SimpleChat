from django.db import models
from django.core import validators

from types import MethodType #拡張メソッド追加用

# Create your models here.

#IDを適当に採番
def get_next(self):
    try:
        lambda: self.objects.latest('pk').id + 1, #順に採番
    except:
        return 0

#Modelクラスに追加
models.Model.get_next = MethodType(get_next, models.Model)


class Users(models.Model):
    INSITE_STATE = (
        (1,'入室中'),
        (2,'退室'),
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
        talk_text = models.CharField(
            verbose_name = '発言',
            max_length = 200,
            default = '',
            )

        user_id = models.ForeignKey(Users,on_delete=models.SET_DEFAULT,default=0)

        talk_datetime = models.DateField('発言日時')

class Chat_Log(models.Model):
        talk_id = models.ForeignKey(Talk,on_delete=models.SET_DEFAULT,default=0)

        talk_text = models.CharField(
            verbose_name = '発言',
            max_length = 200,
            )

        user_id = models.ForeignKey(Users,on_delete=models.SET_DEFAULT,default=0)

        talk_datetime = models.DateField('発言日時')