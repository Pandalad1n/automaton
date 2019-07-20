# Generated by Django 2.1.2 on 2019-04-29 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automaton', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
