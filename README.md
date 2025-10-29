# Programación integrada. Programando para multiples versiones de python

## Objetivo

El objetivo de la practica es crear un programa que devuelva la media de una lista de números y testearlo con pytest. 

Una posible solución
```python
def media(numbers):
    return sum(numbers) / len(numbers)              
```
Al pasar el pytest en local funciona porque utilizan python3, pero en github actions saldra que los test fallan en python2.

```python
def media(numbers):
    return sum(numbers) / float(len(numbers))
```


El yaml de github action esta preparado para ejecutar dichos tests en versiones diferentes de python y en python2 no funciona por lo que da un error.


