# Generated by Django 3.1.3 on 2020-11-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default='cd', max_length=2),
        ),
    ]
