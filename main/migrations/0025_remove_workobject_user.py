# Generated by Django 4.2.1 on 2023-05-10 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_workobject_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workobject',
            name='user',
        ),
    ]