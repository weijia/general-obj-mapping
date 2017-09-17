from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, ForeignKey, PositiveIntegerField
from django.utils.translation import ugettext_lazy as _


class MappingRelation(Model):
    source_content_type = ForeignKey(ContentType, verbose_name=_('source content type'),
                                     related_name="source_content_type")
    source_object_id = PositiveIntegerField(_('source object id'), db_index=True)
    source = GenericForeignKey('source_content_type', 'source_object_id')
    target_content_type = ForeignKey(ContentType, verbose_name=_('target content type'),
                                     related_name="target_content_type")
    target_object_id = PositiveIntegerField(_('target object id'), db_index=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
