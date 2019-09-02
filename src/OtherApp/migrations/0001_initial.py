# Generated by Django 2.2.2 on 2019-07-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('friendUrl', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500, verbose_name='公告')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='通知时间')),
            ],
        ),
    ]