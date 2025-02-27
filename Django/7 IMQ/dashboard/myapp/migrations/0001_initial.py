# Generated by Django 5.0.7 on 2024-09-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('image', models.FileField(default='', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('course', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('inquiryby', models.CharField(max_length=100)),
                ('total_fee', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
