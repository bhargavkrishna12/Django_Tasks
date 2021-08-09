# Generated by Django 3.2.5 on 2021-07-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomType', models.CharField(choices=[('normal', 'Normal'), ('Ac', 'Ac'), ('Delux', 'Delux')], max_length=10)),
                ('num_of_guests', models.IntegerField()),
                ('Fullname', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('mob', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
