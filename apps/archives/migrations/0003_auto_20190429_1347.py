# Generated by Django 2.1.8 on 2019-04-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0002_auto_20190418_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='document',
        ),
        migrations.RemoveField(
            model_name='text',
            name='page',
        ),
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.SlugField(default='replace_me', max_length=191, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='slug',
            field=models.SlugField(default='replace_me', max_length=191, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(default='replace_me', max_length=191, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='replace_me', max_length=191, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]
