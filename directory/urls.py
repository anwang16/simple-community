from django.conf.urls import patterns, url
from views import UserListView, UserDetailView, UserUpdateView

urlpatterns = patterns('',
    url(r'^$', UserListView.as_view()),
    url(
        r'^(?P<pk>[\w]+)$',
        UserDetailView.as_view(),
        name='user-detail'
    ),
    url(
        r'^(?P<pk>[\w]+)/update$',
        UserUpdateView.as_view(),
        name='user-update'
    ),
)
