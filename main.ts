function wypisz_liste(lista_do_wypisania: number[]) {
    serial.writeString("[")
    for (let ktory_element_listy = 0; ktory_element_listy < lista_do_wypisania.length; ktory_element_listy++) {
        serial.writeNumber(lista_do_wypisania[ktory_element_listy])
        serial.writeString(", ")
    }
    serial.writeLine("]")
}

let lista = [7, 9, 5, 8, 3, 6]
let cos2 = 0
let temp2 = 0
let cos3 = 1
function sortowanie() {
    let temp: number;
    
    for (let index = 0; index < lista.length; index++) {
        if (lista[cos2] > lista[cos3]) {
            temp = lista[cos2]
            lista[cos2] = lista[cos3]
            lista[cos3] = temp
            cos2 += 1
            cos3 += 1
        } else {
            temp2 += 1
        }
        
    }
}

wypisz_liste(lista)
for (let index2 = 0; index2 < 1000; index2++) {
    if (temp2 < lista.length) {
        sortowanie()
        wypisz_liste(lista)
        cos2 = 0
        cos3 = 1
        temp2 = 0
    }
    
}
function posortuje_liste(lista_do_posortowania: number[]) {
    //  Tutaj coś trzeba zrobić
    
}

