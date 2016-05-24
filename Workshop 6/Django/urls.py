urlpatterns = patterns('',
    url(r'^$', 'mysite.views.home'),
    url(r'^product$', 'mysite.views.listproducts'),
)