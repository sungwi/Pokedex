# Generated by Django 5.0.6 on 2024-06-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemonapp', '0006_pokemon_ability_alter_pokemon_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
