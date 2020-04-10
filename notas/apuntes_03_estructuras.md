# Estructuras de datos
## Los arrays. 
Las lista de elementos, son arrays, será el nombre usado, para referirnos a
estos elementos. 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',"Julio","Agosto","Octubre","Septiembre","Noviembre","Diciembre"]
```
### Posiciones en un array
Los arrays en python parten de la posición en cero por consiguiente podemos 
acceder alcontenido señalando la posición en (1-n), siendo n la posición a la 
que queremos acceder, por ejemplo si accedemos a n = 1 , la posición será la 0.
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
months[3]="JOJO" # ['Enero', 'Febrero', 'Marzo', 'JOJO', 'Mayo', 'Junio']
print(months[0]) # Enero
print(months[3]) # JOJOJO
```
### Mutable y ordenable
En esta parte ya entramos en el campo de que los arrays son **mutables**, lo 
que quiere decir que son modificables una vez que son creados y en caso 
contrario de que no se puedan modificar una vez creados se consideran
 **inmutables**. 
Por otra parte es un objeto **ordenable** que significa que es un objeto en el que
podemos acceder directamente al valor señalando su posición.

### Igualar contenido
Cabe destacar que cuando igualamos una variable a otra respeto a los arrays en 
Python no estamos creando dos variables iguales haciendo referencia a dos 
elementos distintos, de forma independiente, sino que son dos variables 
apuntando al mismo contenido.
Si sabemos algo de C, del que parten los lenguajes más grandes que hay en el 
mundo del desarrollo. Trabaja con posiciones de memoria. Las variables 
apuntan a posiciones de memoria que almacenan dicho contenido, por 
consiguiente, cuando nosotros en Python igualamos dos variables estamos 
apuntando esas variables a la misma posición de memoria.
```PHP
$listaUna = $listaDos = ["hola","que","tal"];
$listaUna = [];
var_dump($listaUno,$listaDos);
// [],["hola","que","tal"]
```
Por otra parte
```PHP
$listaUna = ["hola","que","tal"];
$listaDos = &$listaUna ; 
$listaDos = []
var_dump($listaUno,$listaDos);
// [],[]
```
En Python es lo mismo.

### Formas de trabajar con listas o arrays
Podemos trabajar de distintas maneras, por ejemplo: 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',"Julio","Agosto","Octubre","Septiembre","Noviembre","Diciembre"]
print(months[1]) # Febraro
```
Por otra parte : 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',"Julio","Agosto","Octubre","Septiembre","Noviembre","Diciembre"]
print(months[-1]) # Diciembre
```
### Slice, o coger parte del array e introducirlo en otro
Podemos *sustraer* por llamarlo así, parte de un array, ejemplo : 
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',"Julio","Agosto","Octubre","Septiembre","Noviembre","Diciembre"]
print(months[0:2]) # ['Enero', 'Febrero']
```
También podemos preguntar si existe un elemento en una array, coomo en php con
la función `in_array`, con las palabras `in` y `not in`, ejemplo :
```python
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',"Julio","Agosto","Octubre","Septiembre","Noviembre","Diciembre"]
print('Diciembre' in months) # True
print('Xamaín' not in months) # True
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

Los diccionarios, son un par de clave y valor. Es como un array con claves de PHP.
Pero se comporta como si fuera un obejto de Javascript. Soporta **not** y **in**. 
Las claves usadas en los diccionarios son **inmmutables**, los elementos
 **inmutables son** por ejemplo, el **int**, **string**, **float**.

```python
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
```

