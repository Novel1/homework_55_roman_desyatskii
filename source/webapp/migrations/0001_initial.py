# Generated by Django 4.1.7 on 2023-02-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('status', models.CharField(max_length=100, verbose_name='Статус')),
                ('created_at', models.DateTimeField(max_length=3000, verbose_name='Дата')),
            ],
        ),
    ]
