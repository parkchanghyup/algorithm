#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))

