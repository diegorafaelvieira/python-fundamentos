# Projeto: Validador de senha
# Regras:
# - A senha deve ter no mínimo 8 caracteres.
# - A senha não pode ser 12345678
# o resultador esperado é dizer se a senha é válida ou não.

password = input("Digite a senha: ")

if password != "12345678" and len(password) >= 8:
  print("Senha válida")
elif len(password) < 8:
  print("Senha inválida! Menos de 8 caracteres")
elif password == "12345678":
  print("Senha inválida! É uma sequência")
