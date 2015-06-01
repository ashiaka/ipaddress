from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.login_successful', name='login_successful'),
    url(r'^register$', 'accounts.views.register', name='register'),
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^login_successful$', 'accounts.views.login_successful', name='login_successful'),
    url(r'^logout$', 'accounts.views.logout', name='logout'),
    url(r'^change_password$', 'accounts.views.change_password', name='change_password'),
)
