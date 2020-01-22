# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:32:07 2019

@author: Franz
"""
from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from .views import home, custom_login, new_invitation, accept_invitation, SignUpView

urlpatterns=[
    path('home', home, name="player_home"),
    path('login',
         custom_login,
         name="player_login"),
    path('logout',
         LogoutView.as_view(),
         name="player_logout"),
    path('new_invitations',
         new_invitation,
         name="player_new_invitation"),
    re_path(r'accept_invitation/(?P<id>\d+)$',
            accept_invitation,
            name="player_accept_invitation"),
    path('signup', SignUpView.as_view(), name="player_signup"),
    ]
