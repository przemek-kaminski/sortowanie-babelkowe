def wypisz_liste(lista_do_wypisania: List[number]):
    serial.write_string("[")
    for ktory_element_listy in range(len(lista_do_wypisania)):
        serial.write_number(lista_do_wypisania[ktory_element_listy])
        serial.write_string(", ")
    serial.write_line("]")

lista = [7, 9, 5, 8, 3, 6]
# lista = [1, 2, 3, 4, 5, 6]

cos2 = 0
czy_byla_zamiana = 0

def sortowanie():
    global cos2, czy_byla_zamiana
    for index in range(lista.length):
        if lista[cos2] > lista[cos2+1]:
            temp = lista[cos2]
            lista[cos2] = lista[cos2+1]
            lista[cos2+1] = temp
            czy_byla_zamiana += 1
        cos2 += 1

wypisz_liste(lista)

while czy_byla_zamiana > 0:
    sortowanie()
    wypisz_liste(lista)
    cos2 = 0
    czy_byla_zamiana = 0

def posortuje_liste(lista_do_posortowania: List[number]):
    # Tutaj coś trzeba zrobić
    pass
