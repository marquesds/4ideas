from django.conf.urls import url

urlpatterns = [
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':'accounts:login'}, name='logout'),
    url(r'^join-us/', 'accounts.views.join', name='join'),
]
