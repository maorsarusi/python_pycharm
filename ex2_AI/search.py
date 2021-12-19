# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:47:43 2020

@author: מאור סרוסי
"""
#search
# זהו הפתרון של תרגיל 1 והוא מימוש בפייתון לפסיאודוקוד שהוצג בכיתה

from ex2_AI import state
from ex2_AI import frontier

def search(n):
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f[1], f[2]]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0

answer=search(3)
print(answer)
