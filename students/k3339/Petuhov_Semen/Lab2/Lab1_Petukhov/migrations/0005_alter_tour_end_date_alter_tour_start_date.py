# Generated by Django 5.1.2 on 2024-11-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab1_Petukhov', '0004_remove_tour_payment_conditions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='end_date',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='tour',
            name='start_date',
            field=models.CharField(max_length=5),
        ),
    ]