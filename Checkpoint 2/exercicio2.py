n = int(input("Digite a quantidade de produtos: "))
i = 1
maiorPreco = float(0)
maiorPorcentagem = float(0)
produtoMaiorPorcentagem = 0
produtoMaiorAumento = 0

while i <= n:
  precoAtual = float(input("Digite o preço atual do " + str(i) + "° produto: "))
  novoPreco = float(input("Digite o novo preço do " + str(i) + "° produto: "))
  diferencaPrecoProdutoAtual = novoPreco - precoAtual
  porcentagemProdutoAtual = diferencaPrecoProdutoAtual / precoAtual * 100
  if diferencaPrecoProdutoAtual > maiorPreco and porcentagemProdutoAtual > maiorPorcentagem:
    maiorPorcentagem = porcentagemProdutoAtual
    maiorPreco = diferencaPrecoProdutoAtual
    produtoMaiorAumento = produtoMaiorPorcentagem = i
  elif diferencaPrecoProdutoAtual < maiorPreco and porcentagemProdutoAtual > maiorPorcentagem:
    maiorPorcentagem = porcentagemProdutoAtual
    produtoMaiorPorcentagem = i
  else:
    maiorPreco = diferencaPrecoProdutoAtual
    produtoMaiorAumento = i
  i = i+1

print("O produto com o maior aumento em reais foi o produto: " + str(produtoMaiorAumento), end=" ")
print("com o aumento de R$"+str(maiorPreco), end=" ")
print("e o produto com o maior aumento percentual foi o produto: "+str(produtoMaiorPorcentagem), end=" ")
print("com o aumento de "+str(maiorPorcentagem)+"%")
