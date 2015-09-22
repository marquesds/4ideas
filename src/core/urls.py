from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'core.views.home', name='home'),
]
