# Generated by Django 4.1.7 on 2023-02-26 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=100)),
                ('destinatario', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]