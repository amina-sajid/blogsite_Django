# Generated by Django 4.0.5 on 2022-06-15 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloggerz', '0004_post_created_on_post_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
