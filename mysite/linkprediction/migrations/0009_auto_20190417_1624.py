# Generated by Django 2.1.7 on 2019-04-17 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkprediction', '0008_auto_20190417_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': '电影'},
        ),
        migrations.AlterModelOptions(
            name='range',
            options={'verbose_name': '年龄'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': '评分'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户'},
        ),
    ]