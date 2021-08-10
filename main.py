def wypisz_liste(lista_do_wypisania: List[number]):
    serial.write_string("[")
    for ktory_element_listy in range(len(lista_do_wypisania)):
        serial.write_number(lista_do_wypisania[ktory_element_listy])
        serial.write_string(", ")
    serial.write_line("]")

moja_lista = [7, 9, 5, 8, 3, 6]
inna_lista = [1, 4, 5, 7, 2]
# lista = [1, 2, 3, 4, 5, 6]

def posortuj(lista: List[number]):
    czy_byla_zamiana = 1
    while czy_byla_zamiana > 0:
        czy_byla_zamiana = 0
        for i in range(lista.length):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                czy_byla_zamiana = 1        

wypisz_liste(moja_lista)
posortuj(moja_lista)
wypisz_liste(moja_lista)


