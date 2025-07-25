# Generated by Django 5.2.3 on 2025-07-05 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('comment_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post_id', models.IntegerField()),
                ('comment_text', models.TextField()),
            ],
        ),
    ]
