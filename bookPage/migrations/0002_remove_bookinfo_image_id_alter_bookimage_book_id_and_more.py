# Generated by Django 5.1.3 on 2024-11-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='image_id',
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='book_id',
            field=models.IntegerField(verbose_name='书id'),
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='图片id'),
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='image',
            field=models.CharField(max_length=200, verbose_name='图片链接'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book_id',
            field=models.IntegerField(verbose_name='书id'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=200, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='评论id'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_id',
            field=models.IntegerField(verbose_name='用户id'),
        ),
    ]