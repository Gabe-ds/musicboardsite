# Generated by Django 3.2.8 on 2021-10-20 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('J-POP', 'J-POP'), ('K-POP', 'K-POP'), ('ANISON', 'ANISON'), ('ROCK', 'ROCK'), ('JAZZ', 'JAZZ')], max_length=12)),
                ('song', models.CharField(max_length=64)),
                ('artist', models.CharField(max_length=64)),
                ('music', models.URLField()),
                ('subtitle', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'board',
            },
        ),
        migrations.CreateModel(
            name='PosterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=2048)),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicboard.boardmodel')),
            ],
            options={
                'db_table': 'poster',
            },
        ),
    ]
