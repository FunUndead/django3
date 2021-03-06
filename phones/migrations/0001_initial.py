# Generated by Django 3.2.6 on 2021-08-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.IntegerField()),
                ('lte_exists', models.TextField()),
                ('slug', models.TextField()),
            ],
        ),
    ]
