# Generated by Django 4.0.5 on 2022-10-17 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0002_alter_comment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='phoneAdd',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
