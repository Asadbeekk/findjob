# Generated by Django 5.1.3 on 2024-12-04 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0003_signin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='email',
            new_name='emaill',
        ),
        migrations.RenameField(
            model_name='signin',
            old_name='password',
            new_name='passwordd',
        ),
    ]
