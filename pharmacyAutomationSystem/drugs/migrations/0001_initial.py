# Generated by Django 4.0.4 on 2022-05-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='product name')),
                ('price', models.PositiveIntegerField(verbose_name='product price')),
                ('stock', models.PositiveIntegerField(verbose_name='product stock')),
                ('quantity', models.PositiveIntegerField(verbose_name='product quantity')),
            ],
        ),
    ]