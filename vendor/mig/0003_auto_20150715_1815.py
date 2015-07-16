# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20150714_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resid',
            name='logo',
            field=models.ImageField(default=b'logo/logo_default.svg', upload_to=b'logo/'),
        ),
    ]
