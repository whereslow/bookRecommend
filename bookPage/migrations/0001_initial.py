# Generated by Django 5.1.3 on 2024-11-26 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_id', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='名称')),
                ('details', models.CharField(max_length=5000, verbose_name='详情')),
                ('image_id', models.IntegerField(verbose_name='图片id')),
                ('other', models.CharField(max_length=5000, verbose_name='其他')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]