# Generated by Django 3.1.3 on 2020-12-23 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_auto_20201223_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image_upload',
            name='user_id',
        ),
        migrations.AddField(
            model_name='image_upload',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
