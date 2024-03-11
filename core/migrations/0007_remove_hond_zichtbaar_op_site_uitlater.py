# Generated by Django 5.0.3 on 2024-03-11 09:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_hond_zichtbaar_op_site'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hond',
            name='zichtbaar_op_site',
        ),
        migrations.CreateModel(
            name='Uitlater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naamUitlater', models.CharField(max_length=100)),
                ('plaats', models.CharField(max_length=100)),
                ('gebruiker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
