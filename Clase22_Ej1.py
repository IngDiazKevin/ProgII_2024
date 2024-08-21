#Clases Abstractas
"""
Un C.Abs.- Es aquella que no se puede instanciar.
Por ejemplo la clase Fig Geo. tendra el metodo
"Calcular Area" como Abst. Ya que el procedimiento
para el calculo no se lo conoce hasta crear un objeto
de la clase hija.

Por ejemplo, clases hijas seran Cuadrado y Rectang
dentro de estas clases tendran cual es el calculo
para del Area.
(cada clase tendra su propio metodo).

Pero la clase padre tambien tendra el metodo para
el calculo de area pero. no tendra la implemetacion
por tanto sera un metodo abstracto.

Al tener el metodo abstracto la clase FigGeo, se 
convierte en una clase abstracta.

Esto implica en que no se puede crear objetos de
una clase definida como abstracta.

Solo se puede crear objetos de las clases hijas
y llamar a los metodos desde las clases hijas.
"""