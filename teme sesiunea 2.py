# reverse the order of the items in an array
lista_unu = [1, 2, 3, 4, 5]


def Reverse(list):
    list.reverse()
    return list


print(Reverse(lista_unu))

# number of occurrences

lista_doi = [1, 1, 1, 1, 4, 4, 6, 7, 9, 9, 9, 3]


def NumberOfOccu(var, list):
    occ = 0
    for i in list:
        if i == var:
            occ += 1
    return occ


var = 6
print(NumberOfOccu(var, lista_doi))

# number of words

string = "numaram cate    cuvinte avem   in propozitia asta     "


def Words(string):
    words = 1
    for i in range(len(string)-1):
        if string[i] == " " and string[i+1] != " ":
            words += 1
    return words


print(Words(string))
