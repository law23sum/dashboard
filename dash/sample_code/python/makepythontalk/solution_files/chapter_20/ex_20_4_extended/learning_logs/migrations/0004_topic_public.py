# Generated by Django 4.1.6 on 2023-02-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
