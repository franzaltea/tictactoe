# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:36:02 2019

@author: Franz
"""
from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'tictactoe/welcome.html')
