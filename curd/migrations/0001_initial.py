# Generated by Django 4.0.3 on 2022-10-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Image', models.ImageField(upload_to='')),
                ('Description', models.TextField()),
            ],
        ),
    ]
