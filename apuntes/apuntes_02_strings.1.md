# Los Strings

## `count` 
Ocurrencias en una palabra en un string

```python
    veces = verse.count("river")
```
## `format`
Para mostrar contenido en un string podemos mostrarlo de distintas formas, por medio de concatenación con el `+` o 
concatenando con un `.` con `format`.
```python
anhos = 10;
print("Tengo {} años".format(anhos))
``` 
## `find` 
Para buscar un elemento en un string

```python
    index = verse.find("stole",0,longitud)
```
## `len` 
Las letras dentro de un string

```python
   longitud = len(verse) 
```
## `lower`
Esta función pone en minúsculas la palabra
## `rfind`
Para buscaro de forma inversa , desde el final al principio

```python
    index = verse.rfind("river",0,longitud)
```## `replace`
Para sustituir letras o pedazos de textos dentro del propio string.