# Generated by Django 5.1.2 on 2024-11-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100)),
                ('name_ja', models.CharField(max_length=100)),
                ('id_number', models.IntegerField()),
                ('image_url', models.URLField()),
                ('type', models.JSONField()),
                ('genus', models.CharField(default='unknown', max_length=100)),
                ('text', models.TextField(default=None)),
                ('ability', models.JSONField(default=[])),
                ('height', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
            ],
        ),
    ]
