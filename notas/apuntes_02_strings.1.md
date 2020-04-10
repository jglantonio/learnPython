# Los Strings

## `len` 
Las letras dentro de un string

```python
   longitud = len(verse) 
```

## `find` 
Para buscar un elemento en un string

```python
    index = verse.find("stole",0,longitud)
```

## `rfind`
Para buscaro de forma inversa , desde el final al principio

```python
    index = verse.rfind("river",0,longitud)
```

## `count` 
Ocurrencias en una palabra en un string

```python
    veces = verse.count("river")
```
## `title`
La función `title` lo que hace es poner el nombre capitalizado.
Otras funciones para strings :
```python
    lista = ['perro','gato','conejo']
    for elemento in lista :
        print(elemento.title())
    # Perro
    # Gato
    # Conejo
```
## `lower`
Esta función pone en minúsculas la palabra
## `replace`
Para sustituir letras o pedazos de textos dentro del propio string.