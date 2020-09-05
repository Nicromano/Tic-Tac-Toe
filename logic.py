# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:33:25 2020

@author: NICROMANO
"""

import rx

observable = rx.from_list([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]) #-1 vacio 1 para x y 0 para o
observable.subscribe(lambda value: print(value))

