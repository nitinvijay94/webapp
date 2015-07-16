# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_auto_20150715_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resid',
            name='logo',
            field=models.ImageField(default=b'logo/PandaLogo.png', max_length=60, upload_to=b'logo/'),
        ),
    ]
