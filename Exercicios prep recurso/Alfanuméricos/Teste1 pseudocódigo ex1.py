texto = input ("Qual é o texto?")
contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0
contadorTotal = 0
vogais = "aeiou"
vogaisTransformadas = "@€!0V"
novoTexto = ""

for i in range (0,len((texto))):
    caracter = texto[i]
    eVogal = vogais.find(caracter)
    if (eVogal != -1):
        caracter = vogaisTransformadas[eVogal]
        if eVogal == 0:
            contadorA += 1
            contadorTotal += 1
        elif eVogal == 1:
            contadorE += 1
            contadorTotal += 1
        elif eVogal == 2:
            contadorI += 1
            contadorTotal += 1
        elif eVogal == 3:
            contadorO += 1
            contadorTotal += 1
        else:
            contadorU += 1
            contadorTotal += 1
    novoTexto += caracter
print ("Texto forma vogais transformadas:", novoTexto)
print("Foram efetuadas as seguintes ", contadorTotal, " Transformacoes")
print ("@ ", contadorA)
print ("€ ", contadorE)
print ("! ", contadorI)
print( "0 ", contadorO)
print ( "V ", contadorU)
