# Generated by Django 4.2.7 on 2023-12-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_author_remove_note_name_alter_note_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
