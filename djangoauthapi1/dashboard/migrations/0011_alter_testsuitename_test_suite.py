# Generated by Django 4.0.3 on 2024-02-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_remove_testsuite_test_suite_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuitename',
            name='test_suite',
            field=models.CharField(max_length=50, verbose_name='Test Suite'),
        ),
    ]
