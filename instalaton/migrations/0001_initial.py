# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('serial', models.CharField(max_length=50, serialize=False, verbose_name=b'Serial', primary_key=True)),
            ],
        ),
    ]
