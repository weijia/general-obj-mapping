from django.views.generic import TemplateView
from django_tables2 import RequestConfig

from djangoautoconf.ajax_select_utils.channel_creator_for_model import get_low_case_model_class_name
from general_obj_mapping.forms import SourceTargetSelectForm, FilterSelectForm
from general_obj_mapping.models import MappingRelation
from general_obj_mapping.tables import MappingRelationshipTable, MappingCreatorTable
from one_lab_enhancement.models import NsnUpperLevelTeam, CurrentJiraBusiness


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


class MappingCreatorView(TemplateView):
    template_name = 'general_obj_mapping/mapping.html'
    item_per_page = 5
    source_model = NsnUpperLevelTeam
    target_model = CurrentJiraBusiness

    def get_context_data(self, **kwargs):
        # self.source_model.objects.filter()
        ctx = super(MappingCreatorView, self).get_context_data(**kwargs)
        form = FilterSelectForm(self.request.GET, initial={"item_per_page": self.item_per_page})
        ctx["form"] = form
        # if form.is_valid():
        #     mapping = MappingRelation.objects.filter(source_content_type=form.cleaned_data["source_content"],
        #                                              target_content_type=form.cleaned_data["target_content"])
        if form.is_valid():
            t = MappingCreatorTable(self.source_model, self.target_model, self.source_model.objects.all())
            RequestConfig(self.request, paginate={"per_page": form.cleaned_data["item_per_page"]}).configure(t)
            # t = MappingCreatorTable(NsnUpperLevelTeam.objects.all())
            ctx["table"] = t
            ctx["target_autocomplete_url"] = '/ajax_select/ajax_lookup/%s' % \
                                             get_low_case_model_class_name(self.target_model)
        else:
            ctx["table"] = None
            ctx["target_autocomplete_url"] = ''
        return ctx
