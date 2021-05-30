acao = int(input ("Quer 1.Comprar ou 2.Vender"))
if(acao == 1):
    tipo = input("Tipo de produto (P)rata (O)uro P(L)atina?")
    quantidade = int(input("Qual a quantidade?"))
    print("**************************************")
    if tipo == "P":
        valorA = 0.41*quantidade
        valorI = valorA*0.23
        valorP = valorA + valorI
    elif tipo == "O":
        valorA = 29.78*quantidade
        valorI = valorA*0.23
        valorP = valorA+valorI
    else:
        valorA = 23.91*quantidade
        valorI = valorA*0.23
        valorP = valorA+valorI
    print("Valor a pagar = ",valorP)
    print ("Antes de Iva = ",valorA)
    print("Valor do Iva ", valorI)
    print("***************************************")
else:
    tipo = input("Tipo de produto (P)rata (O)uro P(L)atina?")
    quantidade = int(input("Qual a quantidade?"))
    print("**************************************")
    if(tipo == "P"):
        valorA = 0.32*quantidade
        valorI = valorA*0.23
        valorR = valorA+valorI
    elif(tipo == "O"):
        valorA = 26.78*quantidade
        valorI = valorA*0.23
        valorR = valorA+valorI
    else:
        valorA = 18.93 * quantidade
        valorI = valorA * 0.23
        valorR = valorA + valorI
    print("Valor a receber = ", valorR)
    print("Antes de Iva = ",valorA)
    print("Valor do Iva = ",valorI)
    print("***************************************")