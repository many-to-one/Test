# Generated by Django 4.2.1 on 2023-05-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_totalworkobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalworkobject',
            name='obj_coffee_food',
            field=models.CharField(default=0.0, max_length=100, null=True, verbose_name='Kawa/Posiłki'),
        ),
        migrations.AlterField(
            model_name='totalworkobject',
            name='obj_fuel',
            field=models.CharField(default=0.0, max_length=100, null=True, verbose_name='Paliwo'),
        ),
        migrations.AlterField(
            model_name='totalworkobject',
            name='obj_phone_costs',
            field=models.CharField(default=0.0, max_length=100, null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='totalworkobject',
            name='obj_prepayment',
            field=models.CharField(default=0.0, max_length=100, null=True, verbose_name='Zaliczka'),
        ),
    ]