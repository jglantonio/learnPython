# Listas comprimidas
Se puede comprimir los bucles `foreach` en una sola linea, siguiendo la siguiente 
estructura, donde podemos si deseamos concatenar `if` :
> new_list = [expression for member in iterable if condition]
```python
    arr = [
        {
            "nombre": "Pepe",
            "nota" : 5
        },{
            "nombre": "Paco",
            "nota" : 7
        },{
            "nombre": "Ramón",
            "nota" : 4
        },{
            "nombre": "Flor",
            "nota" : 2
        }
    ]
    arrAprobados = [e for i, e in enumerate(arr) if e['nota'] >= 5];
    print(arrAprobados)
```
