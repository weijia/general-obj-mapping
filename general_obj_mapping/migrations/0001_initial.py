# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MappingRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_object_id', models.PositiveIntegerField(verbose_name='source object id', db_index=True)),
                ('target_object_id', models.PositiveIntegerField(verbose_name='target object id', db_index=True)),
                ('source_content_type', models.ForeignKey(related_name='source_content_type', verbose_name='source content type', to='contenttypes.ContentType')),
                ('target_content_type', models.ForeignKey(related_name='target_content_type', verbose_name='target content type', to='contenttypes.ContentType')),
            ],
        ),
    ]
