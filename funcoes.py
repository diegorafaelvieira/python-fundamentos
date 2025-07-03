# Funções 
# - Bloquinhos de código que crio e executo quando eu quiser.
# - Conceitos:
# -- Definição da função
# -- Parâmetros
# -- Retorno

def somar(x, y):
  resultado = x + y
  return resultado

print("Minha primeira calculadora:")
soma = somar(10, 7)
print(f"Total: {soma}")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = somar(numero1, numero2)
print(f"Resultado: {soma}")