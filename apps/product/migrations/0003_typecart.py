# Generated by Django 4.0.5 on 2022-06-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typecart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='type')),
                ('type', models.IntegerField(choices=[(0, 'Men'), (1, 'Women'), (2, 'Accessories'), (3, 'Bags'), (4, 'Watches'), (5, 'Shoes')])),
                ('seasion', models.CharField(max_length=200)),
            ],
        ),
    ]
