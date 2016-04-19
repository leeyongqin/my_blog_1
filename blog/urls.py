from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns


urlpatterns = patterns('blog.views',
    url(r'^blog', view='index', name='index'),
    #url(r'^admin/', include(admin.site.urls)),
   )

urlpatterns += staticfiles_urlpatterns()