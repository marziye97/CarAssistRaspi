# Generated by Django 2.1.5 on 2019-01-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('country', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('road', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Signs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('country', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('road', models.CharField(max_length=50)),
                ('speedlimit', models.IntegerField()),
            ],
        ),
    ]
