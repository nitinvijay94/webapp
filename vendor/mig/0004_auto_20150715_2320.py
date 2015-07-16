# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_auto_20150715_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='resid',
            name='menu',
            field=models.ImageField(default=b'menu/pandamenu.jpeg', max_length=200, upload_to=b'menu/'),
        ),
        migrations.AlterField(
            model_name='resid',
            name='logo',
            field=models.ImageField(default=b'logo/logo_default.svg', max_length=60, upload_to=b'logo/'),
        ),
    ]
