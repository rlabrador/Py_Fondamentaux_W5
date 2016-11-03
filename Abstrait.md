## Typage abstrait


> une classe abstraite : Le duck typing. La notion d'iterable en python est abstrait


On boucle sur :
    for item in container:
        do_something(item)
        
> comme on l'a vu un objet qui a une methode  __iter__()
> et une next() est considere comme un iterable

   class Foo():
       def __iter__(self):
           return self
       def next(self):
           # ceci naturellement est bidon
           return 
           
   foo = Foo()
   isinstance(foo, Iterable)