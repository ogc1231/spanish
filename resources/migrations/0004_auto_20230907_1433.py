# Generated by Django 3.2.21 on 2023-09-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_alter_resource_country_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='resource_type',
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_type_filter',
            field=models.CharField(choices=[('podcast_listen', 'Podcast/Listening'), ('youtube_video', 'YouTube/Video'), ('book_read', 'Book/Reading')], default='normal', max_length=32),
        ),
    ]
