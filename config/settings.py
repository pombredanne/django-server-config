import os
import sys

from django.conf import settings
from django.contrib import admin
from config.utils import make_path, make_url, get_media_paths

media_url = make_url(getattr(settings, 'MEDIA_URL'))
media_path = make_path(getattr(settings, 'MEDIA_ROOT'))

admin_media_url = make_url(getattr(settings, 'ADMIN_MEDIA_PREFIX'))
admin_media_path = make_path(os.path.join(os.path.dirname(admin.__file__), 'media'))

project_name = os.environ['DJANGO_SETTINGS_MODULE'].split('.')[0]
project_file = os.path.abspath(sys.argv[0])

sites = getattr(settings, 'CONFIG_SITES', ['www.example.com'])
redirects = getattr(settings, 'CONFIG_REDIRECTS', ['example.com'])
need_auth = getattr(settings, 'CONFIG_NEED_AUTH', False)

media_paths = get_media_paths()