# Generated by Django 3.2.16 on 2023-01-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='next',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='previous',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]