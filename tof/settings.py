# -*- coding: utf-8 -*-
# @Author: MaxST
# @Date:   2019-10-29 17:39:13
# @Last Modified by:   MaxST
# @Last Modified time: 2019-11-13 17:18:16
from django.conf import settings

DEFAULT_LANGUAGE = getattr(settings, 'DEFAULT_LANGUAGE', 'en') or 'en'

SITE_ID = getattr(settings, 'SITE_ID', None)

# need support siteid
# maybe beter use information about neighbors
FALLBACK_LANGUAGES = {
    SITE_ID: ('en', 'de', 'ru'),
    'fr': ('nl', ),
}
FALLBACK_LANGUAGES = getattr(settings, 'FALLBACK_LANGUAGES', FALLBACK_LANGUAGES)
