# Generated by Django 3.1 on 2020-09-16 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodouct', models.CharField(max_length=50)),
                ('modeel', models.CharField(max_length=50)),
                ('water', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='machine_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('machine_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.machine')),
            ],
        ),
    ]