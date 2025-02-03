# Generated by Django 5.1.5 on 2025-02-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('teacher', 'Преподаватель'), ('student', 'Студент'), ('admin', 'Администратор')], default='student', max_length=50)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
