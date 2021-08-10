def wypisz_liste(lista_do_wypisania: List[number]):
    serial.write_string("[")
    for ktory_element_listy in range(len(lista_do_wypisania)):
        serial.write_number(lista_do_wypisania[ktory_element_listy])
        serial.write_string(", ")
    serial.write_line("]")

lista = [7, 9, 5, 8, 3, 6]

cos2 = 0
temp2 = 0
cos3 = 1

def sortowanie():
    global cos2, cos3, temp2
    for index in range(lista.length):
        if lista[cos2] > lista[cos3]:
            temp = lista[cos2]
            lista[cos2] = lista[cos3]
            lista[cos3] = temp
            cos2 += 1
            cos3 += 1
        else:
            temp2 += 1

wypisz_liste(lista)
for index2 in range(1000):
    if temp2 < lista.length:
        sortowanie()
        wypisz_liste(lista)
        cos2 = 0
        cos3 = 1
        temp2 = 0

def posortuje_liste(lista_do_posortowania: List[number]):
    # Tutaj coś trzeba zrobić
    pass
