# Atividade agenda 5 em Desenvolvimento de Sistemas

# Entrada dos dados do cliente

print ("Nesse Programa iremaos calcular o seu consumo de energia ")
aparelho = (input("Por favor digite o tipo do seu eletrodoméstico,(Ex:Geladeira, TV, Micro-ondas) :  "))
potencia = int(input("Agora precisamos saber a potência do seu aparelho em watts (W):  "))
horas = int(input("Quantas horas por dia seu aparelho fica operando/ligado:  "))

# Processamento de dados

consumo_mensal = (potencia * horas) / 1000
custo_mensal = consumo_mensal * 0.75

print (f"O seu consumo diario utilizando {aparelho} é estimado em média de {consumo_mensal} kWh/mês ")
print (f"Além do mais o seu custo mensal estimado é de R$ {custo_mensal:.2f}")