# Generated by Django 4.0.3 on 2024-02-14 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_testsuite_encrypt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuite',
            name='max_dialect',
            field=models.CharField(default='DIALECT_SMB2_002', max_length=255, validators=[django.core.validators.RegexValidator(message="Dialect should be in the format 'DIALECT_SMB3_1_1'", regex='^[A-Za-z]+_[A-Za-z0-9_]+$')], verbose_name='Max Dialect'),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='min_dialect',
            field=models.CharField(default='DIALECT_SMB3_1_1', max_length=255, validators=[django.core.validators.RegexValidator(message="Dialect should be in the format 'DIALECT_SMB3_1_1'", regex='^[A-Za-z]+_[A-Za-z0-9_]+$')], verbose_name='Min Dialect'),
        ),
        migrations.AlterField(
            model_name='testsuitename',
            name='location',
            field=models.CharField(help_text='Enter folder location', max_length=50, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='testsuitename',
            name='test_suite',
            field=models.CharField(max_length=50, verbose_name='Test Suite'),
        ),
    ]
