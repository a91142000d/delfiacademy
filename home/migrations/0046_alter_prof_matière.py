# Generated by Django 3.2.7 on 2021-11-21 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_prof_matière'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='matière',
            field=models.CharField(max_length=255),
        ),
    ]
