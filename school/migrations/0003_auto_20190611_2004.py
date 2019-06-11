# Generated by Django 2.2.2 on 2019-06-11 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20190608_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['teacher']},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
