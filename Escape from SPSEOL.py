import time as t

# nastaveni
body = 1
time = 1.5

# úvodní hláška
print("-------------------------------------")
print("Vítej ve hře zvané Escape from SPSEOL")
t.sleep(time)
print("Tvým úkolem je dostat se ven ze školy")

# pravidla
print("1) dodržuj kritéria, která jsou stanovena")
print("2) bav se")

t.sleep(time + 3)
while body <= 10:

    # konec hry
    if (body == 0):
        print("Game over")
        t.sleep(time + 2)
        print("---------------")
        raise SystemExit

    # č.1 (ucebna_elm2)
    if (body == 1):
        print("--------------------------------")
        print("Právě se nacházíš v učebně ELM 2")
        print("máš na výběr ze tří cest")
        print("")
        print("pro směr vpravo zadej číslo 1")
        print("pro směr vlevo zadej číslo 2")
        print("pro směr přímo zadej číslo 3")
        t.sleep(time)
        smer = int(input("vyber směr: "))

        # směr vpravo (ucebna_elm3)
        if (smer == 1):
            print("-------------------------")
            print("Vešel jsi do učebny ELM 3")
            t.sleep(time)
            print("")
            print("máš na výběr ze dvou cest")
            print("pro směr vpravo zadej číslo 1")
            print("pro směr zpět zadej číslo 2")
            smer1 = int(input("vyber směr: "))

            # směr zpět
            if (smer1 == 2):
                body = 1

            # směr vpravo (okno_2)
            if (smer1 == 1):
                print("Právě jsi vyskočil z okna")
                t.sleep(time + 1)
                print("skok jsi nepřežil")
                t.sleep(time)
                body = 0

            if (smer1 >= 3):
                print("znovu")
                smer1 = int(input("vyber směr: "))

        # směr vlevo (okno_1)
        if (smer == 2):
            print("Právě jsi vyskočil z okna")
            t.sleep(3)
            print("skok jsi nepřežil")
            t.sleep(time)
            body = 0

        # směr přímo (ucebna_elm1)
        if (smer == 3):
            body = 3

        if (smer >= 4):
            print("znovu")
            smer = int(input("vyber směr: "))

    # č.3 (ucebna_elm1)
    if (body == 3):
        print("-------------------------")
        print("Vešel jsi do učebny ELM 1")
        t.sleep(time)
        print("")
        print("máš na výběr ze dvou cest")
        print("pro směr vpravo zadej číslo 1")
        print("pro směr přímo zadej číslo 2")
        smer = int(input("vyber směr: "))

        # směr vpravo (zkratka do ucebna_praxe)
        if (smer == 1):
            print("Našel jsi zkratku")
            print("ovšem pokud jí chceš využít musíš splnit úkol")
            t.sleep(time)

            # ukol zkratka1
            print(
                "jelikož jsi byl v učebně ELM 1, kde se vyučuje elektrotechnické měření,")
            print("předmět občasně těžký,")
            print("tak je zde otázka zda umíš převést 0,001A na mA?")

            odpoved2 = int(input("odpověď: "))
            if (odpoved2 == 1):
                print("Správná odpověď!")
                print("můžeš užít zkratku")
                body = 5

            else:
                print("Špatná odpověď!")
                t.sleep(time)
                print("pan Losert by tě poslal zpět do 1. třídy,")
                t.sleep(time)
                print("ani na distanční výuku by ses nemohl vymluvit")
                body = 0

            # směr přímo (chodba_pav)
        if (smer == 2):
            body = 4

        if (smer >= 3):
            print("znovu")
            smer = int(input("vyber směr: "))

    # č.4 (chodba_pav)
    if (body == 4):
        print("----------------------------")
        print("Vešel jsi na chodbu před PAV")
        # úkol č.8
        print("pokračovat můžeš když splníš úkol:")
        print("Jaké označení má impedance?")
        odpoved8 = input("odpověď: ")
        odpoved8 = odpoved8.lower()
        j = ['z', 'Z']

        if (odpoved8 in j):
            print("Správná odpověď!")
            print("můžeš pokračovat")
            print("")
            t.sleep(time)
            print("máš na výběr ze tří cest")
            print("pro směr vpravo zadej číslo 1")
            print("pro směr přímo zadej číslo 2")
            print("pro směr vlevo zadej číslo 3")
            smer = int(input("vyber směr: "))

            # směr vpravo (ucebna_pav)
            if (smer == 1):
                print("-----------------------")
                print("Vešel jsi do učebny PAV")
                print("")

                # úkol PAV
                print(
                    "jelikož se nacházíš v učebně PAV, kde se většinou vyučuje předmět automatizace,")
                print("tak je zde otázka zda znáš, jeden typ regulace?")
                odpoved1 = input("odpověď (použíj diakritiku): ")
                odpoved1 = odpoved1.lower()
                x = ["spojitá", "nespojitá"]
                if (odpoved1 in x):
                    print("Správná odpověď!")
                    print("vracíš se zpět na chodbu před PAV")
                    body = 4

                else:
                    print("Špatná odpověď!")
                    t.sleep(time)
                    print("pan Kyselý by se zlobil začni tedy znovu!")
                    body = 0
            # směr přimo (jidelna)
            if (smer == 2):
                body = 5

            if (smer == 3):
                print("-----------------------")
                print("Vešel jsi do učebny MIT")
                print("")
                t.sleep(time)
                print("našel jsi zkratku, odpověz na otázku a budeš jí moct využít: ")
                print("Převeď číslo 1101 B na D")
                odpoved7 = int(input("odpověď: "))
                if (odpoved7 == 13):
                    print("Správná odpověd!")
                    t.sleep(time)
                    print("můžeš využít zkratku")
                    body = 7

                else:
                    print("Špatná odpověď!")
                    print("ALU by jsi nepřekonal")
                    body = 4

            if (smer >= 4):
                print("znovu")
                smer = int(input("vyber směr: "))
        else:
            print("Špatná odpověď!")
            print("vrať se do 2.třídy")
            body = 0

    # č.5 (jidelna)
    if (body == 5):
        print("--------------------")
        print("Vešel jsi do jídelny")
        print("")
        t.sleep(time)
        print("máš na výběr ze dvou cest")
        print("pro směr vpravo zadej číslo 1")
        print("pro směr přímo zadej číslo 2")
        smer = int(input("vyber směr: "))

        # směr vpravo (ucebna_praxe)
        if (smer == 1):
            print("--------------------------")
            print("Vešel jsi do učebny praxí")
            print("")
            t.sleep(time)

            # úkol č.6
            print("Pan Hanina tě načapal a chce, aby jsi řekl")
            print("jaké označení má fázový vodič?")
            odpoved1 = input("odpověď : ")
            y = ["L", "l"]
            if (odpoved1 in y):
                print("Správná odpověď!")
                t.sleep(time)
                print("vracíš se zpět do jídelny")
                body = 5

            else:
                print("Špatná odpověď!")
                t.sleep(time)
                print("číslo 155 bylo vytočeno")
                body = 0

        if (smer == 2):
            print("Pokud chceš pokračovat přímo, tak musíš splnit úkol")
            t.sleep(time)
            print(
                "úkol zní: Dokážeš napsat z kolika obědů je ve školní jidelně na výběr?")
            odpoved3 = int(input("odpověď: "))

            if (odpoved3 == 3):
                print("Správná odpověď!")
                print("posouváš se do další místnosti")
                body = 7

            else:
                print("Špatná odpověď!")
                print("zemřel jsi na nedostatek jídla!")
                body = 0

        if (smer >= 3):
            print("znovu")
            smer = int(input("vyber směr: "))

    # č.7 (chodba_mezi_budovami)
    if (body == 7):
        print("---------------------------------")
        print("Vešel jsi na chodbu mezi budovami")
        print("")
        t.sleep(time)
        print("máš na výběr jednu cestu")
        print("pro směr přímo zadej číslo 1")
        smer = int(input("vyber směr: "))

        if (smer == 1):
            # ukol č.5
            print("pokud chceš pokračovat splň úkol:")
            t.sleep(time)
            print("V jakém roce byla Sametová revoluce?")
            print("")
            t.sleep(time)
            print("a) v roce 1945")
            print("b) v roce 1959")
            print("c) v roce 1989")

            odpoved4 = input("odpověď: ")
            e = ['c', 'C']

            if (odpoved4 in e):
                print("Správná odpověď!")
                body = 8

            else:
                print("Špatná odpověď!")

        if (smer >= 2):
            print("znovu")
            smer = int(input("vyber směr: "))

    # č.8 (vstupní hala)
    if (body == 8):
        print("----------------------------------------------")
        print("Vešel jsi do vstupní haly, už jsi skoro venku!")
        print("")
        t.sleep(time)
        print("máš na výběr ze dvou cestu")
        print("pro směr přímo zadej číslo 1")
        print("pro směr vpravo zadej číslo 2")
        smer = int(input("vyber směr: "))

        if (smer == 1):
            print("Vešel jsi do šatny, jediná cesta je zpět")
            t.sleep(time)
            print("proto aby ses dostal zpět je třeba zodpovedět otázku:")
            print("Jaký se vyučuje jazyk v programovaní?")
            odpoved6 = input("odpověď: ")
            odpoved6 = odpoved6.lower()
            o = ['python']

            if (odpoved6 in o):
                print("Správná odpověď!")
                body = 8

            else:
                print("Špatná odpověď!")
                t.sleep(time)
                print("")
                body = 0

        if (smer == 2):
            print("Opouštíš školu, ale zastavil tě déšť nemáš deštník.")
            t.sleep(time)
            print("")
            print("Deštník získáš, když odpovíš na otázku.")
            t.sleep(time)
            print("Je na škole na výběr z nematuritního předmětu na SPŠE Olomouc?")
            print("ano / ne")

            odpoved5 = input("odpověď: ")
            p = ['ne', 'Ne', 'NE', 'nE']

            if (odpoved5 in p):
                print("Utekl jsi ze školy")
                print("ani déšť tě nezastavil!")
                t.sleep(time)
                print("přežil jsi další den")
                t.sleep(time)
                print("The end")
                print("----------------------------------------------------------")
                raise SystemExit

            else:
                print("Špatná odpověď!")
                t.sleep(time)
                print("zmokl jsi, zítra už nepříjdeš do školy")
                t.sleep(time)
                print("The end")
                print("----------------------------------------------------------")
                raise SystemExit

        if (smer >= 3):
            print("znovu")
            smer = int(input("vyber směr: "))
