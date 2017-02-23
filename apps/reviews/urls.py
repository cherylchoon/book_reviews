from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', login_register),
    url(r'^books$', index, name='reviews_index'),
    url(r'^books/(?P<id>\d+)$', book_info, name='book_info'),
    url(r'^users/(?P<id>\d+)$', user_info, name='user_info'),
    url(r'^books/add$', add_review, name='add_review'),
    url(r'^books/add_review$', create_review, name='create_review'),
    url(r'^books/delete_review$', delete_review, name='delete_review')
]
