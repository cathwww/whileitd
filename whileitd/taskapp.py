while True:
    print("""
         1.
         2.
         3.
         4.
         5.
         6.
         7.
         8.
         10.
         20.
         22.
         31. """)

    valik=input("Sisesta ülesande number (1-5) või 'q' väljumiseks: ")
    if valik == '1':
        i = 0
        kogus = 0 
        while i < 15:
            arv = float(input(f"{i + 1}. arv: "))
            if arv.is_integer() and arv>0:
                kogus += arv
            i += 1
        print("Täisarve:", kogus)
    elif valik == '2':
        try:
            while True:
                A = int(input("Sisesta arv A: "))
                if A > 0:
                    summa = 0
                    for i in range(1, A + 1):
                        summa += 1
                    print("Summa:", summa)
                    break
                else:
                    print("Palun sisesta positiivne täisarv.")
        except ValueError:
                print("Palun sisesta kehtiv täisarv.")
    elif valik == '3':
        korrutis = 1
        for i in range(8):
            arv = float(input(f"Sisesta number {i + 1}: "))
            if arv > 0:
                kogus *= arv
        print("Positiivsete arvude korrutis: ", korrutis)
    elif valik == '4':
        for i in range(10, 21):
            print(f"Arvu ruut {i} on {i ** 2}")
    elif valik == '5':
        N = int(input("Sisesta arv N: "))
        kogus = 0
        negatiivne_arv = 0
        while kogus < N:
            arv=float(input(f"Sisesta arv {kogus + 1}: "))
            if arv < 0:
                negatiivne_arv += arv
            kogus += 1
        print("Negatiivsete arvude summa:", negatiivne_arv)
    elif valik == '6':
        while True:
            for i in range(N):
                while True:
                    try:
                        arv = float(input(f"{i + 1}. arv: "))
                        break
                    except ValueError:
                        print("Palun sisesta kehtiv arv.")
                if arv < 0:
                    print("Negatiivne arv")
                    neg_kogus += 1
                elif arv > 0:
                    print("Positiivne arv")
                    pos_kogus += 1
                else:
                    print("Null")
                    null_kogus += 1
        print(f"Negatiivsete arvude kogus: {neg_kogus}")
        print(f"Positiivsete arvude kogus: {pos_kogus}")
        print(f"Nullide kogus: {null_kogus}")
    elif valik == '7':
        while True: 
            try:
                A = int(input("Sisesta arv A: "))
                B = int(input("Sisesta arv B: "))
                K = int(input("Sisesta arv K: "))
                break
            except ValueError:
                print("Palun sisesta kehtiv täisarv.")
        if A>B:
            print("A peab olema väiksem või võrdne B-ga. Siis vahetame need.")
            A,B=B,A
        print(f"Arvud vahemikus [{A}, {B}], mis on {K}-ga jaguvad:")
        for i in range(A, B + 1):
            if i % K == 0:
                print(i)
    elif valik == '8':
        for tolli in range(1, 21):
            cm = tolli * 2.5
            print(f"{tolli} tolli = {cm} cm")
    elif valik == '10':
        for i in range(10):
            a = float(input(f"Paar {i + 1}. Sisesta esimene arv: "))
            b = float(input(f"Paar {i + 1}. Sisesta teine ​​arv: "))
    
            if a > b:
                print(f"Suurem: {a}. ")
            elif b > a:
                print(f"Suurem: {b}. ")
            else:
                print("Arvud on võrdsed.")
    elif valik == '20':
        kogusumma = 0
        for i in range(1, 51):
          if i % 5 == 0 or i % 7 == 0:
            total_sum += i
        print("Arvude summa, mis jagub 5 või 7-ga:", kogusumma)
    elif valik == '22':
         kokku = 0
         for arv in range(100, 201):
           if arv % 17 == 0:
             kokku += arv
             print("Summa:", kokku)
    elif valik == '31':
        K = int(input("Sisesta kotlettide koguarv: "))
        M = int(input("Sisesta, mitu kotletti mahub ühele pannile: "))
        tais_pannid = 0
        while K >= M:
          tais_pannid += 1
          K -= M
        print(f"Täis pannitäisi tuleb praadida: {tais_pannid}")
        print(f"Viimasele pannile jääb kotlette: {K}")
    elif valik.lower() == 'q':
        break
else:
    print("Viga")

