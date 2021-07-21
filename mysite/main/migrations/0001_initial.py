# Generated by Django 3.2.5 on 2021-07-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date_created', models.DateField(verbose_name='date published')),
                ('medium_link', models.URLField(default='Blog is not available for this project')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('course_link', models.URLField(default='Course is not currently available')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('product_link', models.URLField(default='Product is not available')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('sub_heading', models.TextField()),
                ('description', models.TextField()),
                ('youTube_video_link', models.URLField(default='Video is not available for this project')),
                ('medium_link', models.URLField(default='Blog is not available for this project')),
                ('tech_used', models.CharField(max_length=300)),
                ('gitHub_link', models.URLField(default='Project is not available on Github')),
            ],
        ),
    ]
