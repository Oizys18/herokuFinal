# Generated by Django 2.2.7 on 2019-11-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
                ('runtimes', models.CharField(max_length=10)),
                ('thumbnail_url', models.TextField()),
                ('poster_url', models.TextField()),
                ('trailer_url', models.TextField()),
                ('plot', models.TextField()),
                ('plot_outline', models.TextField()),
                ('movie_cast', models.ManyToManyField(related_name='cast_movies', to='movies.Person')),
                ('movie_directors', models.ManyToManyField(related_name='director_movies', to='movies.Person')),
            ],
        ),
    ]
