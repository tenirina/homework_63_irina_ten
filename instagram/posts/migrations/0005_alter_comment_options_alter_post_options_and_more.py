# Generated by Django 4.1.2 on 2022-10-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='count_comment',
            field=models.IntegerField(default=0, verbose_name='Count commentaries'),
        ),
        migrations.AddField(
            model_name='post',
            name='count_like',
            field=models.IntegerField(default=0, verbose_name='Count like'),
        ),
    ]