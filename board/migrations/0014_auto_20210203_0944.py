# Generated by Django 2.0.13 on 2021-02-03 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20210201_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='classification',
            name='month',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='month',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='departmentgoal',
            name='month',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='personalgoal',
            name='month',
            field=models.CharField(max_length=20, null=True),
        ),
    ]