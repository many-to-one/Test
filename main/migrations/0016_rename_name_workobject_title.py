# Generated by Django 4.2.1 on 2023-05-10 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_worktype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workobject',
            old_name='name',
            new_name='title',
        ),
    ]