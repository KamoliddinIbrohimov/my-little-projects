# Generated by Django 4.1.2 on 2022-11-03 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_telegramuser_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Telegram id'),
        ),
    ]
