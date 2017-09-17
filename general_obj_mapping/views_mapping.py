from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView

from django_auto_filter.table_generator import TableGenerator
from general_obj_mapping.forms import SourceTargetSelectForm
from general_obj_mapping.models import MappingRelation
from general_obj_mapping.table import MappingRelationshipTable


class ObjectMappingView(TemplateView):
    # source_model = User
    # target_model = Group
    template_name = 'general_obj_mapping/mapping.html'

    def get_context_data(self, **kwargs):
        # self.source_model.objects.filter()
        ctx = super(ObjectMappingView, self).get_context_data(**kwargs)
        form = SourceTargetSelectForm(self.request.GET)
        ctx["form"] = form
        mapping = MappingRelation.objects.all()
        if form.is_valid():
            mapping = MappingRelation.objects.filter(source_content_type=form.cleaned_data["source_content"],
                                                     target_content_type=form.cleaned_data["target_content"])
        t = MappingRelationshipTable(mapping)
        ctx["table"] = t
        return ctx
