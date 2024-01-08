from django.urls import path

from . import views
from .views import add_author, add_quote, author_detail

app_name = 'quotes'
urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
    path('author/<int:author_id>/', author_detail, name='author'),
]
