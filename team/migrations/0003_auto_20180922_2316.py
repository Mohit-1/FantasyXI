# Generated by Django 2.1.1 on 2018-09-22 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20180920_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
