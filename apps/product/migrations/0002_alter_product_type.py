# Generated by Django 4.0.5 on 2022-06-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.IntegerField(choices=[(0, 'Men'), (1, 'Women'), (2, 'Accessories'), (3, 'Bags'), (4, 'Watches'), (5, 'Shoes')]),
        ),
    ]
