# Generated by Django 3.2.7 on 2021-11-07 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20211107_0137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demmande',
            old_name='wilaya',
            new_name='numéro',
        ),
        migrations.AddField(
            model_name='demmande',
            name='active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
