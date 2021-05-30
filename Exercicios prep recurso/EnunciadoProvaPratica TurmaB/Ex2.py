nrPessoas = 0
somaIdades = 0
maxIdade = 0
nrInfantil = 0
nrAdultos = 0
nrSeniores = 0

nome = input("Qual o 1º nome? (fim para terminar)")

while nome != "fim":

    nrPessoas += 1
    print ("Qual a idade do ", nome)
    idade = int(input())

    while idade <0 or idade != int(idade):
        print ("Qual a idade do ",nome , "(0-120)")
        idade = int(input())

    if idade > maxIdade:
        maxIdade = idade
        maxNome = nome

    if idade <= 18:
        nrInfantil += 1

    elif idade <= 65:
        nrAdultos += 1
        
    else:
        nrSeniores += 1

    somaIdades += idade
    print ("Qual o nome da ", nrPessoas+1, "º pessoa? (fim para terminar)")
    nome = input()

    while nome == "":
        print ("Qual o nome da ", nrPessoas+1, "º pessoa? (nao vazio e fim para terminar)")
        nome = input()

if nrPessoas == 0:
    print ("Ninguem processado")

else:
    mediaIdades = somaIdades/nrPessoas
    print("Media das Idades = ", mediaIdades, "anos.")
    print ("O mais velho = ", maxNome , "com", maxIdade , "anos")
    percentagemI = (nrInfantil/nrPessoas)*100
    percentagemA = (nrAdultos/nrPessoas)*100
    percentagemS = (nrSeniores/nrPessoas)*100
    print("Ha", percentagemI, "% infantil")
    print("Ha", percentagemA, "% adultos")
    print ("Ha", percentagemS, "% Seniores")
