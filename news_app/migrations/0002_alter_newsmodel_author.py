# Generated by Django 4.2.7 on 2023-11-25 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]