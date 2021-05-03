n = int(input("Digite a quantidade de números na sequência: "))
qtdSequencia = 0
i = 1
m = 0

while i <= n:
  numeroAnterior = m
  m = int(input("Digite o " + str(i) + "° número: "))
  if numeroAnterior != m:
    qtdSequencia = qtdSequencia+1
  i = i+1

print("Quantidade de sequências: " + str(qtdSequencia))
  
