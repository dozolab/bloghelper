# Generated by Django 3.1.2 on 2020-10-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='telegramuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='telegramuser',
            name='step',
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='language_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
