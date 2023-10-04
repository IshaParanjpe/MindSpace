# Generated by Django 4.1.1 on 2022-10-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_journaling_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rec',
            old_name='link',
            new_name='platform',
        ),
        migrations.AddField(
            model_name='blog',
            name='link',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]