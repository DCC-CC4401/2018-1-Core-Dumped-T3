# Generated by Django 2.0.3 on 2018-05-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180502_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]