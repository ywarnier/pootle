# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from django.conf.urls import url

from .views import SocialVerificationView


urlpatterns = [
    url(r'^social/verify/$',
        SocialVerificationView.as_view(),
        name='pootle-social-verify'),
]
