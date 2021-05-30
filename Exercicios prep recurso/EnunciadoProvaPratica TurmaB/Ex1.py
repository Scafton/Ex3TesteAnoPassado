nrPessoas = 0
somaIdades = 0

nome = input("Qual o 1º nome? (fim para terminar)")

while nome != "fim":

    nrPessoas += 1

    print ("Qual a idade do ", nome)
    idade = int(input())
    while idade <0 or idade != int(idade):
        print ("Qual a idade do ",nome , "(0-120)")
        idade = int(input())

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