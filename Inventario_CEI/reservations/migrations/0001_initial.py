# Generated by Django 2.0.5 on 2018-05-07 16:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0005_auto_20180503_1522'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='initial date')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'vigente'), (1, 'caducado'), (2, 'recibido'), (3, 'perdido')], default=0)),
                ('article_or_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='articles.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_loans', to='users.RegisteredUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='initial date')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'pendiente'), (1, 'entregado'), (2, 'rechazado')], default=0)),
                ('article_or_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='articles.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_reservations', to='users.RegisteredUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpaceLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='initial date')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'vigente'), (1, 'caducado'), (2, 'recibido'), (3, 'perdido')], default=0)),
                ('article_or_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='articles.Space')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='space_loans', to='users.RegisteredUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpaceReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='initial date')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'pendiente'), (1, 'entregado'), (2, 'rechazado')], default=0)),
                ('article_or_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='articles.Space')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='space_reservations', to='users.RegisteredUser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
