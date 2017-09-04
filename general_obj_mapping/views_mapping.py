from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView


class ObjectMappingView(TemplateView):
    source_model = User
    target_model = Group

    def get_context_data(self, **kwargs):
        self.source_model.objects.filter()
        ctx = super(ObjectMappingView, self).get_context_data(**kwargs)
        return ctx
