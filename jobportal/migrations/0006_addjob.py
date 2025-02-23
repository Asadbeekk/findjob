# Generated by Django 5.1.3 on 2024-12-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0005_rename_emaill_signin_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('employment_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract'), ('internship', 'Internship'), ('freelance', 'Freelance')], max_length=20)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
