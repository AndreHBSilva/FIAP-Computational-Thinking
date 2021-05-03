cedula = int(input("Digite o valor da cédula: "))
moeda1 = int(input("Digite o valor de uma moeda: "))
moeda2 = int(input("Digite o valor da outra moeda: "))

qtdMoeda1 = 0
qtdMoeda2 = 0
i = cedula

while i > 0:
  if moeda1 > moeda2:
    if i - moeda1 < moeda2 and i - moeda1 != 0:
      i = i - moeda2
      qtdMoeda2 = qtdMoeda2 + 1
    else:
      i = i - moeda1
      qtdMoeda1 = qtdMoeda1 + 1
  else:
    if i - moeda2 < moeda1 and i - moeda2 != 0:
      i = i - moeda1
      qtdMoeda1 = qtdMoeda1 + 1
    else:
      i = i - moeda2
      qtdMoeda2 = qtdMoeda2 + 1
      
if qtdMoeda1 * moeda1 + qtdMoeda2 * moeda2 > cedula:
  print("Não é possível fazer a troca")
else:
  print("Possível: " + str(qtdMoeda1) + " moeda(s) de " + str(moeda1) + " e " + str(qtdMoeda2) +" moeda(s) de " + str(moeda2))
  
  
