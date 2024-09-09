# Generated by Django 5.1.1 on 2024-09-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('sns_image', models.ImageField(upload_to='')),
                ('good', models.IntegerField()),
                ('read', models.IntegerField()),
                ('readtext', models.TextField()),
            ],
        ),
    ]
