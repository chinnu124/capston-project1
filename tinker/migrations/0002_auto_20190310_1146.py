# Generated by Django 2.1.5 on 2019-03-10 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='amount_paid',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='event',
        ),
    ]