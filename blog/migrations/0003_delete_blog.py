# Generated by Django 2.1.1 on 2018-10-02 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
