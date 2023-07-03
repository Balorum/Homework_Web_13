# Generated by Django 4.2.1 on 2023-06-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0007_remove_quote_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='authors',
        ),
        migrations.AddField(
            model_name='quote',
            name='authors',
            field=models.ManyToManyField(to='quoteapp.author'),
        ),
    ]
