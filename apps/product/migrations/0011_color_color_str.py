# Generated by Django 4.0.5 on 2022-06-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_color_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color_str',
            field=models.CharField(max_length=6, null=True),
        ),
    ]