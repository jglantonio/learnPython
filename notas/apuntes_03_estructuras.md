# Estructuras de datos
## Las listas. 
Las lista de elementos, son arrays. 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
```
### Formas de trabajar con listas o arrays
Podemos trabajar de distintas maneras, por ejemplo: 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
print(months[1]) # Febraro
```
Por otra parte : 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
print(months[-1]) # Junio
```
Podemos *sustraer* por llamarlo así, parte de un array, ejemplo : 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
print(months[0:2]) # ['Enero', 'Febrero']
```
También podemos preguntar si existe un elemento en una array, coomo en php con
la función `in_array`, con las palabras `in` y `not in`, ejemplo :
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
print('Diciembre' in months) # False
print('Enero' not in months) # True
```
### Mutabilidad y ordenable

Podemos modificar los arrays si hacemos referencia a su posición en él. Tenemos
que los arrays son **mutables**, lo que quiere decir que son modificables una vez
que son creados y en caso contrario de que no se puedan modificar una vez creados
se consideran **inmutables**. 
Por otra parte es un objeto **ordenable** que significa que es un objeto en el que
podemos acceder directamente al valor señalando su posición.

```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
months[3]="JOJO" # ['Enero', 'Febrero', 'Marzo', 'JOJO', 'Mayo', 'Junio']
print(months[0]) # Enero
```

### Funciones útiles
* `max`, máximo valor en el array, para el caso de **integers** , devolverá el valor máximo, por otra parte par los **strings**, el string más largo. Para el caso de existir distintos tipos de elementos, devolverá un error
* `len`, longitud del array
* `sorted`, ordena los valores de menor mayor o mayor menor.
* `join`, une los elementos de un **array** en un **string**. Lo mismo que con `max` no se puede mezclar typos de elementos, en un mismo array no puede haber **integer** y **string** a la vez.

## Truplas

Las **truplas** son un tipo de dato **mutable** y **ordenables**

```python
dimensions = 23,32,32
dimensions = (23,32,32)
alto, ancho, largo = (23,32,32)
print(dimensions) # (23, 32, 32)
print(alto) # 32
print(ancho) # 32
print(largo) # 32
```

## Sets

Esta estructura de datos son **mutables** y no **ordenables** de obejtos únicos. Podemos transformar un **array** en un **sets** lo que hará será eliminar los elementos duplicados.
```python
animales = ['perro','gato','gallo','unicornio','leopardo','gallo']
print(animales)
setAnimales = set(animales) 
# ['perro', 'gato', 'gallo', 'unicornio', 'leopardo', 'gallo']
print(setAnimales) 
# set(['gato', 'leopardo', 'perro', 'gallo', 'unicornio'])
```
Como podemos ver al no ser **ordenable** no trabaja pudiendo acceder a los 
distintos elementos. Sino usa `add` , `pop`, entre otras funciones, pro ejemplo:
```python
setAnimales.add('cerbatillo')
print(setAnimales)
# set(['leopardo', 'unicornio', 'gato', 'perro', 'cerbatillo', 'gallo'])
setAnimales.pop()
print(setAnimales)
# set(['unicornio', 'gato', 'perro', 'cerbatillo', 'gallo'])
```

## Diccionarios

Los diccionarios, son un par de clave y valor. Es como un array con claves de PHP. Pero se comporta acomo si fuera un obejto de Javascript. Soporta **not** y **in**

