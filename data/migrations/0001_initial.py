# Generated by Django 4.1.4 on 2023-02-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalModel',
            fields=[
                ('serialNumber', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]
