# Generated by Django 2.2.2 on 2019-08-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0008_auto_20190728_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialColumn',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('like_account', models.IntegerField(default=0, verbose_name='点赞')),
            ],
        ),
    ]
