from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns


urlpatterns = patterns('blog.views',
    url(r'', view='index', name='index'),

   )

urlpatterns += staticfiles_urlpatterns()