# Generated by Django 3.2.11 on 2022-02-07 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220205_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='tags',
        ),
    ]