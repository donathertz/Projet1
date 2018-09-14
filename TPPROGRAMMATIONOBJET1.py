#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:07:53 2018

@author: uansi
"""

x=1
y=1
z=1
def f():
  def g():
    z=3
    print(dir(),x,y,z)

  y=2
  print(x,y,z)

  g()

print(x,y,z)
f()
print(x,y,z)