# Generated by Django 4.2.1 on 2023-05-18 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='work_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objekt', to='main.workobject'),
        ),
    ]