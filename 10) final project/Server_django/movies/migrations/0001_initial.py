# Generated by Django 3.2.3 on 2021-05-24 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('vote_count', models.IntegerField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('overview', models.TextField(blank=True)),
                ('poster_path', models.CharField(blank=True, max_length=200)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
