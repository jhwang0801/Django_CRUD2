# Generated by Django 4.0.4 on 2022-05-10 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'actors',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('release_date', models.DateField()),
                ('running_time', models.IntegerField()),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='ActorMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'db_table': 'actors_movies',
            },
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(through='movies.ActorMovie', to='movies.movie'),
        ),
    ]
