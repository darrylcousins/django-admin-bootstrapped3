from django.conf.urls import patterns, include, url

from django.contrib import admin

from CapitalApp.models import CapitalModel
from CapitalApp.views import AutocompleteView

admin.autodiscover()

def get_queries():
    """
    Helper to generate simple api views, filter is the only way in use here
    """
    return ['filter']

def make_api_urls(_urlpatterns, name, model):
    """
    Helper method to generate API urls.
    """
    for query in get_queries():
        _urlpatterns.append(
            url(r'^api/%s/%s/$' % (query, name),
                AutocompleteView.as_view(
                    model=model,
                    query=query
                    ),
                name='%s_api_%s' % (name, query)),
            )
    return urlpatterns

urlpatterns = ['']

urlpatterns = make_api_urls(urlpatterns, 'CapitalApp', CapitalModel)

urlpatterns = urlpatterns + [
    # Examples:
    # url(r'^$', 'test_django_admin_bootstrapped_p3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    ]

urlpatterns = patterns(*urlpatterns)
