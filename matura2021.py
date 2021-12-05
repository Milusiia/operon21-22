import functools as ft


def rozdziel_i_suma_kwadrat(liczba):
    suma = 0
    reszta = liczba % 10
    cale = liczba // 10
    suma += reszta ** 2
    while cale > 0:
        reszta = cale % 10
        cale = cale // 10
        suma += reszta ** 2
    return suma


def rozdziel_i_suma_sprytniej(liczba):
    suma = 0
    for l in str(liczba):
        suma += int(l) ** 2
    return suma


def zsumuj(accumulator, aktualny):
    return accumulator + int(aktualny) ** 2


# to samo co na dole z lambdą => zsumuj == lambda_zsumuj
lambda_zsumuj = lambda accumulator, aktualny: accumulator + int(aktualny) ** 2


def rozdziel_i_suma_oneline(liczba):
    return ft.reduce(lambda_zsumuj, str(liczba), 0)


przyk = 7442
print(rozdziel_i_suma_sprytniej(przyk))
print(rozdziel_i_suma_oneline(przyk))


def algorytm():
    max_dict = {}
    counter = 0
    for x in range(1, 1001):
        # for x in range(1, 1001):
        # print('>>>', x)
        wyniki = []
        wynik_kroku = rozdziel_i_suma_sprytniej(x)
        mam_wynik = False
        pierwszy_przebieg = True
        poprzedni_wynik = -1

        while mam_wynik is False:
            # while not wynik_kroku == 1 or wynik_kroku != pierwszy_wynik_kroku:
            if wynik_kroku == 1:
                print(x, 'liczba jest wesola', wyniki)
                mam_wynik = True
                counter += 1
                wyniki.append(1)
                aktualny_max = max(wyniki)
                if aktualny_max in max_dict:
                    max_dict[aktualny_max].append(x)
                else:
                    max_dict[aktualny_max] = [x]
                print(aktualny_max)
            elif wynik_kroku in wyniki and pierwszy_przebieg is False:
                # print(x, 'liczba jest niewesola')
                mam_wynik = True
            else:
                pierwszy_przebieg = False
                poprzedni_wynik = wynik_kroku
                wynik_kroku = rozdziel_i_suma_sprytniej(wynik_kroku)
                wyniki.append(poprzedni_wynik)
                # print('krok, x:',x, 'pierwszy:', wyniki, 'wynik kroku:', wynik_kroku)
    print('max_dict', max_dict)
    maksy = max_dict.keys()
    print('maksy', maksy)

    max_klucz = max(maksy)
    print('zad 1', max_klucz, max_dict[max_klucz])
    print('liczb wesolych: ', counter)

# algorytm()
