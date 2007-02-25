from django.conf.urls.defaults import *
from django.conf import settings

defaultdict = { 'groupName': 'example' }

urlpatterns = patterns('',
    # Example:
    # (r'^simpleproject/', include('simpleproject.foo.urls')),

    (r'^$', 'django.views.generic.simple.redirect_to', { 'url': '/wiki/show/Start/' }),

    (r'^board/', include('sphene.sphboard.urls'), defaultdict),
    (r'^wiki/', include('sphene.sphwiki.urls'), defaultdict),

    (r'accounts/login/$', 'django.contrib.auth.views.login'),
    (r'accounts/logout/$', 'django.contrib.auth.views.logout' ),

    # Only for development
    (r'^static/sphene/(.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/../../static/sphene' }),

    # Uncomment this for admin:
     (r'^admin/', include('django.contrib.admin.urls')),
)
