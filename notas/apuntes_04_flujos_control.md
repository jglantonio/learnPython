# Flujos de control
## A tener en cuenta
Hay unos conceptos que hay que tener en cuenta en python : 
* En Python no se usan `{}` para acotar los `if`, `for` y un largo etc
  de flujos de control.
* Para identar código se usan 4 espacios para los casos en los que se mire
  implicado `()`, `{}`.

## If .
Tenemos los `if` : 
```python
if condicion :
    # Code
```
Cuando se usa un `else` : 
```python
if condicion :
    # Code
else : 
    # Code
```
Cuando se usa un `else-if` : 
```python
if condicion_a :
    # Code
elif condicion_b :
    # Code
else : 
    # Code
```
# Puertas lógicas

Como pudimos ver como desarrollar un `if` en estas condiciones podemos meter puertas lógicas. Hay que tener los siguientes tips en cuenta : 
* En el caso de Python, no se definen como en PHP, con un `&&` y `||` sinó como son `and` y `or`
* No hace falta igualar a `true` los valores booleanos.
* Trata todos los valores como `true` que no sea `false`.

# Notas

## No hace falta igualar a un booleano

Cuando definimos un boolean o puertas lógicas en un `if` el valor es el mismo. si definimos.
```python
    if valor == true :
        # Codigo
```
Es lo mismo que definir :
```python
    if valor :
        # Codigo
```
# For loops
Python tiene dos tipos de bucles `for` y `while`. Puede recorrer elementos iterables.
```python
    lista = ['perro','gato','conejo']
    for elemento in lista :
        print(elemento)
    # perro
    # gato
    # conejo
```
Para generar listas de elementos integeres podemos ejecutar la función `range(inicio,final,salto)`, si queremos establecer del 1 al 10 de uno al uno simplemente `(range(1,11,1)`.
```python
    for elemento in range(1,11,1) :
        print(elemento)
```
## While

```python
lista = ['perro','gato','conejo']
i = 0
while i < len(lista) :
   print(lista[i])
   i+=1
```
## Más información
 * [PEP 8 : Guía para programar en Python](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
