from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# 导入timezone用于处理时间相关事件
from django.utils import timezone
# 倒入表单模块
from django import forms
# Create your models here.

class InfoPost_7(models.Model):
    # 试题的上传者，参数on_delete用于指定删除的方式
    uploader = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200,default='忘记输入标题')

    # 试题的信息，均设置为字符串字段
    question = models.CharField(max_length=200)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    answer = models.IntegerField()

    # 试题的其他信息
    question_id = models.CharField(max_length=10)
    question_info = models.CharField(max_length=200)

    # 创建时间,设置默认创建时间为当前时间
    created = models.DateTimeField(default=timezone.now)

    # 创建内部类,用作于指定其他信息
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class InfoPost_8(models.Model):
    # 试题的上传者，参数on_delete用于指定删除的方式
    uploader = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200,default='忘记输入标题')

    # 试题的信息，均设置为字符串字段
    question = models.CharField(max_length=200)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    answer = models.IntegerField()

    # 试题的其他信息
    question_id = models.CharField(max_length=10)
    question_info = models.CharField(max_length=200)

    # 创建时间,设置默认创建时间为当前时间
    created = models.DateTimeField(default=timezone.now)

    # 创建内部类,用作于指定其他信息
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class InfoPost_9(models.Model):
    # 试题的上传者，参数on_delete用于指定删除的方式
    uploader = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200,default='忘记输入标题')

    # 试题的信息，均设置为字符串字段
    question = models.CharField(max_length=200)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    answer = models.IntegerField()

    # 试题的其他信息
    question_id = models.CharField(max_length=10)
    question_info = models.CharField(max_length=200)

    # 创建时间,设置默认创建时间为当前时间
    created = models.DateTimeField(default=timezone.now)

    # 创建内部类,用作于指定其他信息
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title