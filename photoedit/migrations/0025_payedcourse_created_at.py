# Generated by Django 4.2.1 on 2023-05-25 08:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photoedit', '0024_remove_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='payedcourse',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
