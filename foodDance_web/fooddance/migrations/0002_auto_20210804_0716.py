# Generated by Django 2.1.5 on 2021-08-04 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fooddance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]