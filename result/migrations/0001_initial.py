# Generated by Django 3.2.9 on 2022-05-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('test_score', models.FloatField()),
                ('merit_score', models.FloatField()),
                ('position', models.IntegerField()),
                ('college', models.CharField(max_length=100)),
                ('selection', models.CharField(max_length=100)),
            ],
        ),
    ]
