# Generated by Django 2.1.5 on 2021-08-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddance', '0004_auto_20210804_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipes'),
        ),
    ]