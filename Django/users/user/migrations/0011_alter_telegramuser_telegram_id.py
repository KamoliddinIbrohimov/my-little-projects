# Generated by Django 4.1.2 on 2022-11-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_userinfo_id_alter_userinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Telegram id'),
        ),
    ]
