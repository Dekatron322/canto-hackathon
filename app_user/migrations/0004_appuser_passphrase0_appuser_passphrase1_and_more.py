# Generated by Django 4.1.3 on 2022-12-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_remove_appuser_passphrase0_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='passphrase0',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase1',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase10',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase11',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase2',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase3',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase4',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase5',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase6',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase7',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase8',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='appuser',
            name='passphrase9',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
