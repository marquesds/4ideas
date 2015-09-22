from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'social.views.timeline', name='timeline'),
]
