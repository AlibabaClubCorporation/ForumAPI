# Generated by Django 4.0.5 on 2022-07-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_usersofclient_date_of_creation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersofclient',
            options={'ordering': ['date_of_creation', 'client', 'username'], 'verbose_name': 'Пользователь клиента', 'verbose_name_plural': 'Пользователи клиентов'},
        ),
    ]