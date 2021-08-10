function wypisz_liste(lista_do_wypisania: number[]) {
    serial.writeString("[")
    for (let ktory_element_listy = 0; ktory_element_listy < lista_do_wypisania.length; ktory_element_listy++) {
        serial.writeNumber(lista_do_wypisania[ktory_element_listy])
        serial.writeString(", ")
    }
    serial.writeLine("]")
}

let lista = [7, 9, 5, 8, 3, 6]
//  lista = [1, 2, 3, 4, 5, 6]
let cos2 = 0
let czy_byla_zamiana = 0
function sortowanie() {
    let temp: number;
    
    for (let index = 0; index < lista.length; index++) {
        if (lista[cos2] > lista[cos2 + 1]) {
            temp = lista[cos2]
            lista[cos2] = lista[cos2 + 1]
            lista[cos2 + 1] = temp
            czy_byla_zamiana += 1
        }
        
        cos2 += 1
    }
}

wypisz_liste(lista)
while (czy_byla_zamiana > 0) {
    sortowanie()
    wypisz_liste(lista)
    cos2 = 0
    czy_byla_zamiana = 0
}
function posortuje_liste(lista_do_posortowania: number[]) {
    //  Tutaj coś trzeba zrobić
    
}

