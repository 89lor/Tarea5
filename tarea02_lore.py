def ordenamiento_seleccion(lista):
  """Ordena una lista de números en orden ascendente."""
  for i in range(len(lista)):
    min_index = i
    for j in range(i + 1, len(lista)):
      if lista[j] < lista[min_index]:
        min_index = j
    lista[i], lista[min_index] = lista[min_index], lista[i]
  return lista
def main():
  """Solicita   que el  usuario  ingrese una serie de números separados por espacios y luego los ordena en orden ascendente."""
  numeros = input("Ingrese una serie de números separados por espacios: ")
  numeros = numeros.split()
  numeros = [int(numero) for numero in numeros]
  numeros_ordenados = ordenamiento_seleccion(numeros)
  print("La lista ordenada es:", numeros_ordenados)
if __name__ == "__main__":
  main()
