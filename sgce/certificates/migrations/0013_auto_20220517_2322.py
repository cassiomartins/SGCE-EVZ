# Generated by Django 2.2.26 on 2022-05-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0012_auto_20220512_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='px_coordinator',
            field=models.IntegerField(blank=True, help_text='Default Value 50', null=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='px_manager',
            field=models.IntegerField(blank=True, null=True, verbose_name='Default Value 35'),
        ),
    ]