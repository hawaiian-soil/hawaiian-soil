# Generated by Django 2.0.2 on 2018-04-27 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0003_auto_20180418_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
