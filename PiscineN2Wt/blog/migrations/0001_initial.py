# Generated by Django 4.2.7 on 2023-11-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=40)),
            ],
        ),
    ]
