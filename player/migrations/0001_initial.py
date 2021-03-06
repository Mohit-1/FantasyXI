# Generated by Django 2.1.1 on 2018-09-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('jersey_number', models.CharField(max_length=2)),
                ('position', models.CharField(choices=[('GK', 'Goalkeeper'), ('DEF', 'Defender'), ('MID', 'Midfielder'), ('FW', 'Forward')], max_length=5)),
                ('valuation', models.FloatField()),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
    ]
