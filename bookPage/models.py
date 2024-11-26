from django.db import models


# Create your models here.


class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, verbose_name='名称')
    # details 用markdown格式
    details = models.CharField(max_length=5000, verbose_name='详情')
    other = models.CharField(max_length=5000, verbose_name='其他')


class BookImage(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='图片id')
    # 一个book有多个图片,id对应
    book_id = models.IntegerField(verbose_name='书id')
    # 外链形式
    image = models.CharField(max_length=200, verbose_name='图片链接')


class Review(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="评论id")
    user_id = models.IntegerField(verbose_name="用户id")
    book_id = models.IntegerField(verbose_name="书id")
    content = models.CharField(max_length=200, verbose_name="评论内容")
    date = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
