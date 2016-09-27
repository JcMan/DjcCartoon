from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('cartoon.views',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index'),
    url(r'^type/(\d+)$', 'cartoontype'),
    url(r'^type/(\d+)/(\d+)$', 'cartoontypeajax'),
    url(r'^catalog/(\d+)$', 'catalog'),
    url(r'^chapter/(\d+)$', 'chapter'),
)
