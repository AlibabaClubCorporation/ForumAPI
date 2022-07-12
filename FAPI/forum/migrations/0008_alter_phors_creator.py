# Generated by Django 4.0.5 on 2022-07-12 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_alter_phors_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phors',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phors', to='forum.usersofclient', verbose_name='Ссылка на создателя фора'),
        ),
    ]
