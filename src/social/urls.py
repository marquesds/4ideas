from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'social.views.timeline', name='timeline'),
    url(r'^post/', 'social.views.post', name='post'),
    url(r'^delete-post/(?P<pk>\d+)/$', 'social.views.delete_post', name='delete_post'),
]
