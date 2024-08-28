# Generated by Django 5.1 on 2024-08-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(default='unit', max_length=20),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
