# Generated by Django 4.2.1 on 2023-05-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_work_over_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='sum_over_time',
            field=models.CharField(default='00:00', max_length=5, null=True, verbose_name='Nadgodziny'),
        ),
    ]