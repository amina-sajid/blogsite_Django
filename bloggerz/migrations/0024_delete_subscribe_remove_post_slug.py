# Generated by Django 4.0.5 on 2022-07-02 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloggerz', '0023_rename_user_subscribe_e_mail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscribe',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
