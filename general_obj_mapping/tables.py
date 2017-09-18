from django.contrib.contenttypes.models import ContentType
from django_tables2 import Column
from django_tables2 import Table
from django_tables2 import TemplateColumn
from django_tables2_reports.tables import TableReport

from general_obj_mapping.models import MappingRelation
from one_lab_enhancement.models import NsnUpperLevelTeam, JiraBusiness


class MappingRelationshipTable(TableReport):
    class Meta:
        model = MappingRelation
        exclude = ["source_content_type", "source_object_id", "target_content_type", "target_object_id"]

    source = Column()
    target = Column()

    # noinspection PyMethodMayBeStatic
    def render_source(self, record):
        return record.source

    # noinspection PyMethodMayBeStatic
    def render_target(self, record):
        return record.target


class MappingCreatorTable(TableReport):
    id = Column()
    source_content_type_id = Column(empty_values=())
    target_content_type_id = Column(empty_values=())
    source = Column(empty_values=())
    target = Column(empty_values=())

    class Meta:
        attrs = {}

    def __init__(self, source_model, target_model, *args, **kwargs):
        self.source_model = source_model
        self.target_model = target_model
        self.target_content_type = ContentType.objects.get_for_model(self.target_model)
        self.source_content_type = ContentType.objects.get_for_model(self.source_model)
        self.Meta.attrs = {"source_content_type_id": self.source_content_type.id,
                           "target_content_type_id": self.target_content_type.id,
                           }
        super(MappingCreatorTable, self).__init__(*args, **kwargs)
        # self.source_model = NsnUpperLevelTeam
        # self.target_model = JiraBusiness

    # # class Meta:
    # #     model = NsnUpperLevelTeam
    # source_model = NsnUpperLevelTeam
    # target_model = JiraBusiness

    # noinspection PyMethodMayBeStatic
    def render_source(self, record):
        return self.source_model.objects.get(id=record.id)

    def render_target(self, record):
        target_object = MappingRelation.objects.filter(
            source_content_type=self.source_content_type,
            source_object_id=record.id,
            target_content_type=self.target_content_type)
        value = ""
        if target_object.exists():
            value = target_object[0].target
        return value

    def render_source_content_type_id(self):
        return self.source_content_type.id

    def render_target_content_type_id(self):
        return self.target_content_type.id
