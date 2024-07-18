# Generated by Django 4.0.5 on 2022-06-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggerz', '0015_rename_post_comment_posts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='null'),
            preserve_default=False,
        ),
    ]
