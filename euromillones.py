from random import sample
def euro():
    for x in range(49):
#lista de  numeros comprendida entre 1 y 50(1,51) y , numeros que necesitamos sample no se repiten
        L=sample(range(1,51),5)
#sorted ordena la lista
        print(sorted(L))
#aqui sacamos dos numeros
        n = sample(range(1,13),2)
        print(sorted(n))
euro()
