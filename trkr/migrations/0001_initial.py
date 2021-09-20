# Generated by Django 3.2.7 on 2021-09-20 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('nick_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('cell_phone', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('cal_minute', models.DecimalField(decimal_places=1, max_digits=7)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('duration', models.DecimalField(decimal_places=1, max_digits=7)),
                ('note', models.CharField(max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='trkr.client')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='trkr.exercise')),
            ],
        ),
    ]