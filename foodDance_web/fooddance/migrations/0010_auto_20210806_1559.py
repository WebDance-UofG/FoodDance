# Generated by Django 2.1.5 on 2021-08-06 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fooddance', '0009_userprofile_has_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmstring',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fooddance.UserProfile'),
        ),
    ]