# Generated by Django 4.0.4 on 2022-05-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='computer_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=10)),
                ('order', models.CharField(max_length=100)),
            ],
        ),
    ]