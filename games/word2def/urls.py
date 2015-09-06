#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from .views import Word2DefQuestionView


urlpatterns = [
    url(r'^play/$', Word2DefQuestionView.as_view(), name='play'),
    url(r'^answer/(?P<uuid>[a-z0-9-]+)/$', Word2DefQuestionView.as_view(), name='answer'),
]

