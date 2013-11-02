from django.conf.urls import patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', 'pina.views.index', name='pina-index'),
)
