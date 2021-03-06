from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^search/$', 'search', name='search'),
    url(r'^feedback/$', 'feedback', name='feedback'),
    url(r'^test_error_email/', 'test_error_email'),
    url(r'^(?P<slug>\w+)\.html', 'page', name='page')
)