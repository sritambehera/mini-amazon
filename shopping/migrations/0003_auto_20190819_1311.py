# Generated by Django 2.2.3 on 2019-08-19 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20190819_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_password',
            new_name='password',
        ),
    ]