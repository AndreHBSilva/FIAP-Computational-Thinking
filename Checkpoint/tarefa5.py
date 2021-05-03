def calcularInss(salario):
  if salario == 0:
    inss = 0
    return inss
  elif salario <= 1100.0:
    inss = 82.5
    return inss
  elif salario <= 2203.48:
    inss = 82.5 + 99.31
    return inss
  elif salario <= 3305.22:
    inss = 82.5 + 99.31 + 132.21
    return inss
  else:
    inss = 82.50 + 99.31 + 132.21 + 27.27
    return inss

salario = float(input("Digite o seu salário: "))
print("INSS: R$ ", round(calcularInss(salario), 2))