# Generated by Django 4.2.7 on 2023-12-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0008_remove_tag_tag_of_username_tag_tag_of_username'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='tag of username',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='nametag',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='tag of username'),
        ),
    ]