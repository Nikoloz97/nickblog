# Generated by Django 5.1.7 on 2025-05-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='comment',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
