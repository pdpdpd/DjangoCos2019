# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models


# what is duck typing?


# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True, max_length=50, default="", verbose_name=u"Main_key")
    name = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name=u"Username")
    email = models.EmailField(verbose_name=u"Email")
    address = models.CharField(max_length=100, verbose_name=u"Address")
    message = models.CharField(max_length=500, verbose_name=u"Message")

    # models.ForeignKey
    # models.DateTimeField
    # models.IntegerField
    # models.IPAddressField
    # models.FileField
    # models.ImageField
    class Meta:
        verbose_name = u"UserMessageContent"
        verbose_name_plural = verbose_name
        #db_table = "user_message"
        #ordering = "-object_id"
        #for making tables