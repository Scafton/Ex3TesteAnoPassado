idade = int(input("Qual a sua idade?"))
tipoC = input("Qual o tipo de consulta? (O)ftalmologia, (P)siquiatria, (C)ardiologia ou (D)ermatologia")
if tipoC =="O":
    if idade<=12:
        desconto = 80*0.15
        pagar = 80-desconto
    elif idade>=65:
        desconto = 80*0.25
        pagar = 80-desconto
elif tipoC == "P":
    if idade<=12:
        desconto = 95*0.15
        pagar = 95-desconto
    elif idade>=65:
        desconto = 95*0.25
        pagar = 95-desconto
else:
    if idade<=12:
        desconto = 75*0.15
        pagar = 75-desconto
    elif idade>=65:
        desconto = 75*0.25
        pagar = 75-desconto
print("Vai pagar = ", pagar, " euros.")
