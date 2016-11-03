## Surcharge d'opérateurs


> une surcharge d'opérateurs
> C'est redéfinir une méthode dans une sous-classe définie dans une super-classe
> une surcharge d'opérateurs est une redféinition de méthode définie par le language pour totue les classes
> Ces méthodes servent à manipuler les classes que l'on créé comme les objets built-in (print, ex...)

    __init__ est une surcharge buit-in

    class C:
    def set_x(self, x):
        self.x = x
    def get_x(self):
    print self.x


    I=C()
    
    I.get_x()
> renvoit une erreur : #AttributeError: C instance has no attribute 'x'

> Il faut donc redéfinir un constructeur de type built-in __init__


    class C:
    def __init__(self):
        print 'dans C'
        self.x = 0
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

> Ici I.get_x() renvoit maintenant 0

> On peut aussi passer des argument à un constructeur !!



    class C:
    def __init__(self, a):
        print 'dans C'
        self.x = a
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

    I = C(10)
> Ici l'espace de nommage renvoit bien 10 : {'x':10}

> Voyons maintenant comment définir une classe dérivée. Il faut ici appeler explicitiement le constructeur des classés principales dans l'init

    class D(C):
        def __init__(self):
            C.__init__(self,a)
            print 'dans D'

    I = D(140)
> L'exécution donne dans C, dans D

> L'espace de nommage est quant à lui toujours indépendant est renvoie :
> {'x': 140}

> N'oublions pas qu'enfin une méthode surchargée __str__ existe et est en charge d'afficher automatiquement le retour de la fonction print


    class C:
    def __init__(self, a):
        print 'dans C'
        self.x = a
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x
    def __str__(self):
        return str(self.x)

    I = C(10)
    print I --> retourne 10
    J = D(30)
    print J --> retourne 30

> Il existe plus de 80 opérateurs buit-in qui permettent de Surcharger  'print', in, +, -, *,/, <,>, ==, etc. mais aussi les séquences en utilisant la notion de crochets S[i]
> Ces opérateurs permettent d'étendre le language pour donner sens à des fragments de code.
> ex: item in object
> object[key]
>if object:
> object.key

