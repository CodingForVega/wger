# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-01 14:38
from __future__ import unicode_literals

from django.db import migrations, models

def copy_username(apps, schema_editor):
    '''
    Copies the exercise name to the original name field
    '''
    Ingredient = apps.get_model("nutrition", "Ingredient")
    for ingredient in Ingredient.objects.all():
        if ingredient.user:
            ingredient.license_author = ingredient.user.username
        else:
            ingredient.license_author = 'wger.de'
        ingredient.save()

def update_status(apps, schema_editor):
    '''
    Updates the status of the ingredients
    '''
    Ingredient = apps.get_model("nutrition", "Ingredient")
    Ingredient.objects.filter(status__in=('5', '4')).update(status=2)

class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='order',
            field=models.IntegerField(blank=True, editable=False, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='order',
            field=models.IntegerField(blank=True, editable=False, verbose_name='Order'),
        ),
        migrations.RunPython(copy_username, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(update_status, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='ingredient',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')], default='1',
                                   editable=False, max_length=2),
        ),
    ]
