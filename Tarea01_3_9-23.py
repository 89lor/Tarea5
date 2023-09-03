def calcular_imc(peso, altura):
  """Calcula el índice de masa corporal (IMC) de una persona.
  Args:
    peso: El peso de la persona en kilogramos.
    altura: La altura de la persona en metros.
  Returns:
    El IMC de la persona.
  """
  imc = peso / (altura ** 2)
  return imc
def imprimir_categoria_imc(imc):
  """Imprime una categoría basada en el IMC calculado.
  Args:
    imc: El IMC de la persona.
  """
  if imc < 18.5:
    print("Bajo peso")
  elif 18.5 <= imc < 25:
    print("Peso normal")
  elif 25 <= imc < 30:
    print("Sobrepeso")
  else:
    print("Obesidad")
# Obtener el peso y la altura del usuario.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
# Calcular el IMC del usuario.
imc = calcular_imc(peso, altura)
# Imprimir la categoría del IMC del usuario.
imprimir_categoria_imc(imc)

