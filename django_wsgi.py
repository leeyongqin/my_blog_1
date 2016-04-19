#!/usr/bin/env python
# coding: utf-8

import os
import sys
from django.core.wsgi import get_wsgi_application

# 将系统的编码设置为UTF8
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()
