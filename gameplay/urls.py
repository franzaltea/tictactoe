# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:58:36 2019

@author: Franz
"""
from django.urls import path, re_path

from .views import game_detail, make_move, AllGamesList

urlpatterns = [
    re_path(r'detail/(?P<id>\d+)/$',
        game_detail,
        name="gameplay_detail"),
    re_path(r'make_move/(?P<id>\d+)/',
            make_move,
            name="gameplay_make_move"),
    path('all', AllGamesList.as_view()),
    ]
