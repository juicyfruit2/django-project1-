# Generated by Django 4.2.1 on 2023-05-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('signature', models.CharField(default='joshua', max_length=140)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
