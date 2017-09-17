from django.conf.urls import patterns, url

from general_obj_mapping.views_filter_and_mapping import FilterAndMappingView
from general_obj_mapping.views_mapping import ObjectMappingView

urlpatterns = patterns('',
                       url(r'^filter/', FilterAndMappingView.as_view()),
                       url(r'^$', ObjectMappingView.as_view()),
                       )
