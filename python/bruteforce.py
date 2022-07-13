import random


armi = ["Carta","sasso","forbici"]
for arma in armi:
    print(arma)
print("premi 0 carta, 1 per sasso, 2 forbici")
numero_scelto = int(input())
arma_scelta = armi[numero_scelto]
print("hai scelto: " + arma_scelta)

arma_dell_avversario = ""
if arma_scelta == "carta":
    arma_dell_avversario = "forbice"
if arma_scelta == "sasso":
    arma_dell_avversario = "carta"
if arma_scelta == "forbici":
    arma_dell_avversario = "sasso"
risposta = input()
print("l'avversario ha scelto" + arma_dell_avversario + "\n" )
