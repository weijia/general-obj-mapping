from django.conf.urls import patterns, url

from general_obj_mapping.views_filter_and_mapping import ObjectFilteringByContentType
from general_obj_mapping.views_mapping import ObjectMappingView, MappingCreatorView

urlpatterns = patterns('',
                       url(r'^filter/', ObjectFilteringByContentType.as_view()),
                       url(r'^mapper/', MappingCreatorView.as_view()),
                       url(r'^$', ObjectMappingView.as_view()),
                       )
