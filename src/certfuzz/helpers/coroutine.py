'''
Created on Jul 16, 2014

@author: adh
'''


#from http://www.dabeaz.com/coroutines/coroutine.py
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start
