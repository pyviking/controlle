# Generated by Django 3.0.5 on 2020-05-01 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_auto_20200501_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lancamentoconta',
            name='lembrar',
        ),
    ]
