# Generated by Django 2.1.7 on 2019-03-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('team', '0006_remove_team_captain'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='captain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.Player'),
        ),
    ]
