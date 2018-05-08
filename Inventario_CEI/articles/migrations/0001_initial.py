# Generated by Django 2.0.5 on 2018-05-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(default='articles/images/items/', upload_to='articles')),
                ('description', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Disponible'), (1, 'En préstamo'), (2, 'En reparación'), (3, 'Perdido')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Disponible'), (1, 'En préstamo'), (2, 'En reparación')], default=0)),
            ],
        ),
    ]
