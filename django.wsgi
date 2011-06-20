import os
import sys

path = '/home/shauns/py'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djproj.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
