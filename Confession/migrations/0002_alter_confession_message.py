# Generated by Django 4.0 on 2022-01-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Confession', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confession',
            name='message',
            field=models.TextField(),
        ),
    ]