# Generated by Django 3.2.7 on 2021-11-15 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.formation'),
        ),
    ]