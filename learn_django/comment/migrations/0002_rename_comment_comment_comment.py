# Generated by Django 4.2.16 on 2024-09-15 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="Comment",
            new_name="comment",
        ),
    ]
