# Generated by Django 4.0.3 on 2022-10-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0002_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40)),
                ('Image', models.ImageField(upload_to='media/Blog')),
                ('Description', models.TextField()),
            ],
        ),
    ]
