import sys
import os.path
  
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
  
import sae
from app import wsgi
  
application = sae.create_wsgi_app(wsgi.application)
