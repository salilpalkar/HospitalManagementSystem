# Generated by Django 3.0.6 on 2020-05-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('specialization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('is_receptionist', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_hr', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
