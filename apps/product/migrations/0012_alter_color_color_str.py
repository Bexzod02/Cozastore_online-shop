# Generated by Django 4.0.5 on 2022-06-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_color_color_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color_str',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]