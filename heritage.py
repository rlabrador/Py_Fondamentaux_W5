#-*- coding: utf-8 -*-
#Moin fichier à pousser
class C1:
    pass

class C2:
    pass

class C3(C1, C2):
    def func(self):
        self.x = 10

#Des classes qui héritent de super classe --> on créé alors un arbre d'héritage', qui sert à la recherche d'attribut'
#On a donc un lien entre l'espace de noammge (L'endroit ou vivent les variables) et l'arbre d'héritage
I1 = C3()
I2 = C3()

#Exemple
#Ne pas oublier le self qui doit prendre un argument au méthode qui est l'instance même 
#super classe
class C:
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x


#sous classe
class sousC(C):
    def get_x(self):
        print 'x est :',self.x


c = C()

sc =sousC();


c.__class__
sc.__class__
sousC.__bases__
#retourne un tuple des superclass associées à l'instance'
c.set_x(10)
sc.set_x(20)
#Vérifions les espaces de nommage (dict)

c.__dict__
#renvoit {'x': 10}
sc.__dict__
#renvoit {'x': 20}

#Si on regarde sur la méthodde get_x()

c.get_x()
sc.get_x()
#Ceux sont bien deux métohdes différentes qui sont appelées
#en python  tout est un objet, et les classes et les instances sont des objets mutables
#En python on peut donc dynamiquement rajouter des méthodes aux classes

def f(self):
    print 'depuis C', self.x


C.get_x = f
#C'est une fonction qui 
c.get_x()


#Plusieurs formes d'héritage pour les méthodes :
#(Implicite) : Si la classe fille ne définit pas du tout la méthode.
#Redéfinie : si on écrit la méthode entièrement.
#Modifiée : Si on récrit la méthode dans la classe fille, mais en utilisant le code de la classe mère.


# Une classe mère
class Fleur(object):
    def implicite(self):
        print 'Fleur.implicite'
    def redefinie(self):
        print 'Fleur.redefinie'
    def modifiee(self):
        print 'Fleur.modifiee'


# Une classe fille
class Rose(Fleur):
    # on ne definit pas implicite
    # on redefinit complement redefinie
    def redefinie(self):
        print 'Rose.redefinie'
    def modifiee(self):
        super(Rose, self).modifiee()
        print 'Rose.modifiee apres Fleur'    


fille = Rose()
fille.modifiee()
#renvoit : 
# Fleur.modifiee                                                                                                                                                                              
# Rose.modifiee apres Fleur   


#Héritage vs Composition
        

# Une classe avec qui on n'aura pas de relation d'héritage
class Tige(object):
    def implicite(self):
        print 'Tige.implicite'
    def redefinie(self):
        print 'Tige.redefinie'
    def modifiee(self):
        print 'Tige.modifiee'

# on n'hérite pas
# mais on fait ce qu'on appelle un composition
# avec la classe Tige
class Rose(object):
    # mais pour chaque objet de la classe Rose
    # on va créer un objet de la classe Tige
    # et le conserver dans un champ
    def __init__(self):
        self.externe = Tige()

    # le reste est presque comme tout à l'heure
    # sauf qu'il faut definir implicite
    def implicite(self):
        self.externe.implicite()
        
    # on redefinit complement redefinie
    def redefinie(self):
        print 'Rose.redefinie'
        
    def modifiee(self):
        self.externe.modifiee()
        print 'Rose.modifiee apres Tige'       