# Generated by Django 3.2.7 on 2021-10-24 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_commande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='date_commande',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='validé',
        ),
    ]
