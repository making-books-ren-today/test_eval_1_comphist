# Generated by Django 2.1.8 on 2019-05-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0004_auto_20190429_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box',
            options={'ordering': ['number']},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['doc_id']},
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'ordering': ['full']},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last', 'first']},
        ),
        migrations.AddField(
            model_name='document',
            name='doc_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]