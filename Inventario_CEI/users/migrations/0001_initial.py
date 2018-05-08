# Generated by Django 2.0.5 on 2018-05-08 21:53

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
            name='RegisteredUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='users/images/default-profile.png', upload_to='')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Préstamos y Reservas'), (1, 'Sólo préstamos'), (2, 'Sólo reservas'), (3, 'Nada')], default=0)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
