# Generated by Django 4.0 on 2021-12-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0005_stage_bs_color_alter_client_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='slug',
            field=models.CharField(default='stage', max_length=50, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='bs_color',
            field=models.CharField(max_length=50, verbose_name='Цвет по категориям боотстрап'),
        ),
    ]
