# Generated by Django 5.0.7 on 2024-09-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_remove_post_content_remove_post_feature_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('coding', 'Coding'), ('health', 'Health'), ('travel', 'Travel')], max_length=10, null=True),
        ),
    ]
