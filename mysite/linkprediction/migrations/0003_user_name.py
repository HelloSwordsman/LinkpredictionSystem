# Generated by Django 2.1.7 on 2019-04-08 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkprediction', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=128, verbose_name='姓名'),
            preserve_default=False,
        ),
    ]