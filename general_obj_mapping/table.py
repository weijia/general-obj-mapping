from django_tables2 import Column
from django_tables2 import Table
from django_tables2_reports.tables import TableReport

from general_obj_mapping.models import MappingRelation


class MappingRelationshipTable(TableReport):
    class Meta:
        model = MappingRelation
        exclude = ["source_content_type", "source_object_id", "target_content_type", "target_object_id"]

    source = Column()
    target = Column()

    def render_source(self, record):
        return record.source

    def render_target(self, record):
        return record.target
