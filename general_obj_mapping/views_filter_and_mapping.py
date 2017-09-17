from django.contrib.contenttypes.models import ContentType

from django_auto_filter.views_django_auto_filter import DjangoAutoFilter
from general_obj_mapping.forms import FilterSelectForm


class ObjectFilteringByContentType(DjangoAutoFilter):
    template_name = "general_obj_mapping/filter_and_mapping.html"

    def get_context_data(self, **kwargs):
        is_content_type_selected = False
        content_type_filter_form = FilterSelectForm(self.request.GET)
        if content_type_filter_form.is_valid():
            source_content_type = content_type_filter_form.cleaned_data["source_content"]
            self.request.session["filtering_content_type"] = \
                {"source_content": source_content_type.id}
            is_content_type_selected = True
        elif "filtering_content_type" in self.request.session:
            content_type_filter_form = FilterSelectForm(self.request.session["filtering_content_type"])
            if content_type_filter_form.is_valid():
                source_content_type = content_type_filter_form.cleaned_data["source_content"]
                is_content_type_selected = True

        if is_content_type_selected:
            self.model = source_content_type.model_class()
            ctx = super(ObjectFilteringByContentType, self).get_context_data(**kwargs)
            ctx["is_content_type_selected"] = True
        else:
            ctx = super(DjangoAutoFilter, self).get_context_data(**kwargs)
            ctx["is_content_type_selected"] = False
            del self.request.session["filtering_content_type"]
        ctx["content_type_filter_form"] = content_type_filter_form
        return ctx
