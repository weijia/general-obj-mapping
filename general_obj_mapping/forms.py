from django.contrib.contenttypes.models import ContentType
from django.forms import Form, ModelChoiceField, IntegerField


class SourceTargetSelectForm(Form):
    source_content = ModelChoiceField(queryset=ContentType.objects.order_by('model'))
    target_content = ModelChoiceField(queryset=ContentType.objects.order_by('model'))


class FilterSelectForm(Form):
    source_content = ModelChoiceField(queryset=ContentType.objects.order_by('model'))
    target_content = ModelChoiceField(queryset=ContentType.objects.order_by('model'), required=False)
    item_per_page = IntegerField(initial=5)
