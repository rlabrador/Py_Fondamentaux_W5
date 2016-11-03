## Typage et instance


> une classe classique

    class OldStyle: 
        pass
> une instance

    old_style = OldStyle()

> son type est juste 'instance'

    type(old_style)
> renvoit 'instance'


> une classe new-style : elle hérite de 'object'

    class NewStyle(object): 
        pass
> une instance de cette classe

    new_style = NewStyle()

> le type de l'instance est bien la classe

    type(new_style) is NewStyle
> Renvoit : True !!!