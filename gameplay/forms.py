# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:35:56 2019

@author: Franz
"""
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Move

class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = []
    
    def clean(self):
        # DEBUG cleaned_data is where the form data gets stored
        x = self.cleaned_data.get("x")
        y = self.cleaned_data.get("y")
        game = self.instance.game
        try:
            if game.board()[y][x] is not None:
                raise ValidationError("Square is not empty")
        except IndexError:
            raise ValidationError("Invalid coordinates")
            return self.cleaned_data
