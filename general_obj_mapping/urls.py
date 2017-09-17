from django.conf.urls import patterns, url
from general_obj_mapping.views_mapping import ObjectMappingView

urlpatterns = patterns('',
                       url(r'^$', ObjectMappingView.as_view()),
                       )
