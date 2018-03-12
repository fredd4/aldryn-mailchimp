# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from aldryn_mailchimp.views import campaign_detail

urlpatterns = [
    url(
        r'^(?P<pk>[0-9]+)/(?P<slug>[\w.@+-]+)/$',
        campaign_detail,
        name='mailchimp_campaign_detail'
    ),
)
