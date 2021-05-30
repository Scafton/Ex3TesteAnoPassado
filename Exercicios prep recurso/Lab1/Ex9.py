nrCriancas = int(input("Quantas crianças/Jovens existem no agregado?"))
rendimento = float(input("Qual o rendimento do agregado?"))
rendimentoRef = rendimento/nrCriancas+1
if(rendimentoRef<= 8803.62):
    print ("O rendimento de ref desta familia e ", rendimentoRef, " euros")
else:
    print("Esta familia nao tem rendimento de ref")