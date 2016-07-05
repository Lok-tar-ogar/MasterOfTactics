#encoding:utf-8
from django.db import models

class adv(models.Model):
    title=models.CharField('标题',max_length=50)
    content=models.CharField('内容',max_length=500)
    language=models.CharField('语言',max_length=500,default='en',choices=(('en','英文'),('rs','俄文'),('fr','法文'),('gr','德文')))
    act_date=models.DateTimeField('活动结束时间',null=True)
    dim_date=models.DateTimeField('添加时间',auto_now_add=True)

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = "广告"
        ordering = ['id']

    def __str__(self):
        return self.title
