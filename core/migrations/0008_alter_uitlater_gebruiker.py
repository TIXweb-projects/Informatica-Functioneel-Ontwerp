# Generated by Django 5.0.3 on 2024-03-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_hond_zichtbaar_op_site_uitlater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uitlater',
            name='gebruiker',
            field=models.CharField(max_length=100),
        ),
    ]
