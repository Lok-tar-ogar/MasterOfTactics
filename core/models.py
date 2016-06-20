#encoding:utf-8
from django.db import models

class adv(models.Model):
    title=models.CharField('标题',max_length=50)
    content=models.CharField('内容',max_length=500)
    act_date=models.DateTimeField('活动结束时间',null=True)
    dim_date=models.DateTimeField('添加时间',auto_now_add=True)

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = "广告"
        ordering = ['id']

    def __str__(self):
        return self.title
