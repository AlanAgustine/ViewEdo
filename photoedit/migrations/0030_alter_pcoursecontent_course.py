# Generated by Django 4.2.1 on 2023-05-25 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoedit', '0029_alter_pcoursecontent_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcoursecontent',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_content', to='photoedit.payedcourse'),
        ),
    ]
