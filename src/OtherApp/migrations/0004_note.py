# Generated by Django 2.2.2 on 2019-08-10 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0008_remove_useraccount_access_last_time'),
        ('OtherApp', '0003_auto_20190804_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=1000)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='留言时间')),
                ('type', models.PositiveIntegerField(choices=[(1, '公开留言'), (0, '私信'), (2, '建议')], default=1, verbose_name='留言类型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='UserApp.UserAccount', verbose_name='用户')),
            ],
        ),
    ]