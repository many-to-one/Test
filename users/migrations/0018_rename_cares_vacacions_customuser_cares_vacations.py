# Generated by Django 4.2.1 on 2023-06-16 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_customuser_force_majeure_vacations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='cares_vacacions',
            new_name='cares_vacations',
        ),
    ]