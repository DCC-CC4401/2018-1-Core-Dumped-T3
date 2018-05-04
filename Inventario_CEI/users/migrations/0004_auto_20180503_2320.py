# Generated by Django 2.0.4 on 2018-05-03 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180503_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='id',
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
