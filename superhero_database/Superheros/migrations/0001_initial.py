# Generated by Django 3.1.7 on 2021-04-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alter_ego', models.CharField(max_length=50)),
                ('primary_superhero_ability', models.CharField(max_length=50)),
                ('secondary_superhero_ability', models.CharField(max_length=50)),
                ('catch_phrase', models.CharField(max_length=50)),
            ],
        ),
    ]
