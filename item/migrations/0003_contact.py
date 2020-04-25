# Generated by Django 3.0.3 on 2020-04-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=255)),
                ('mailid', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=1000)),
            ],
        ),
    ]
