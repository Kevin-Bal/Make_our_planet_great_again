# Generated by Django 2.2.17 on 2020-12-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateforme', '0006_auto_20201223_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='dateFinancement',
            field=models.DateTimeField(),
        ),
    ]
