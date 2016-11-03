#-*- coding: utf-8 -*-
#Surcharge

class C:
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

I = C()

I.get_x()
## exception(, *args, **kwargs) : I.get_x()
#AttributeError: C instance has no attribute 'x'

#Il faut définir un constructeur avec un type buit-in __init__

 




