# Generated by Django 3.0 on 2019-12-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prisoner',
            name='id_number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Id Number'),
        ),
    ]
