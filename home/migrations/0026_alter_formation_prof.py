# Generated by Django 3.2.7 on 2021-10-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.prof'),
        ),
    ]
