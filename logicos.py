# 4 == 4 -> True
# 3 != 3 -> False
# 3 > 2 -> True
# 4 < 20 -> True
# 10 >= 5 -> False
# 3 <= 3 -> True

idade = 17
if idade >= 12 and idade < 18:
  print("É um adolescente")
elif idade >= 18:
  print("É um adulto")
elif idade < 12:
  print("É uma criança")


if idade == 17 or (idade >=21 and idade < 25):
  print("Pode se alistar")
else:
  print("Não pode se alistar")