
def solucion1(data):
    dataArray = data.split()
    cantidad = []
    len = len(dataArray)
    contador = 0
    while(contador != len):
        lista = dataArray.count(str(dataArray[contador]))
        cantidad.append(dataArray[contador] + str(lista))
        contador = contador + 1 
    cantidadSet = list(dict.fromkeys(cantidad))
    solucion = ""
    for c in cantidadSet:
        solucion = solucion + c 
        
    return solucion

# "#" Incrementa el valor numérico en 1.
# "@" Decrementa el valor numérico en 1.
# "*" Multiplica el valor numérico por sí mismo.
# "&" Imprime el valor numérico actual.

def solucion2(valor):
    resultado = 0
    valorArray = list(valor)
    final = ""
    for char in valorArray:
        if char == '#':
            resultado = resultado + 1
        elif char == '@':
            resultado = resultado - 1
        elif char == '*':
            resultado = resultado * resultado
        elif char == '&':
            final = final + str(resultado)
    return final




