name = input("Qual o seu nome? ").title()
age = int(input("Qual a sua idade? "))
# Aqui é um comentário em uma linha 
# VS Code: Selecionar e ctrl + /
print("------")
print(f"O seu nome é {name} ({len(name)} caracteres) e você tem {age + 1} anos.")