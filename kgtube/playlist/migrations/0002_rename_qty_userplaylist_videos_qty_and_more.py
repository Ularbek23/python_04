# Generated by Django 4.2.7 on 2023-11-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userplaylist',
            old_name='qty',
            new_name='videos_qty',
        ),
        migrations.RenameField(
            model_name='userplaylist',
            old_name='views',
            new_name='views_qty',
        ),
        migrations.RemoveField(
            model_name='userplaylist',
            name='discription',
        ),
        migrations.AddField(
            model_name='userplaylist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userplaylist',
            name='name',
            field=models.CharField(max_length=55),
        ),
    ]
