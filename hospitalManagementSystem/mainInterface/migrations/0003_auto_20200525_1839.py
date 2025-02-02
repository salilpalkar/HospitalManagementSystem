# Generated by Django 3.0.6 on 2020-05-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0002_auto_20200525_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='HR',
        ),
        migrations.DeleteModel(
            name='Receptionist',
        ),
    ]
