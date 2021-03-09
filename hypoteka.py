# VSTUPY
def get_data(): # získej vstupy
    vypujcena_castka = int(input("Kolil sis pučil?: "))
    leta_splaceni = int(input("Za kolik let to splatíš?: "))
    mesice_splaceni = leta_splaceni * 12
    mesicni_urok = float(input("S jakým úrokem?: "))
    return vypujcena_castka, mesicni_urok, mesice_splaceni

# MATIKA
def matika(vypujcena_castka,mesicni_urok,mesice_splaceni):   # matika bere data z fce get_data()
    r = mesicni_urok/100/12     # tohle moc nevim co je a jak to srozumitelně pojmenovat
    mesicni_splatka = round(vypujcena_castka*(r*(1+r)**mesice_splaceni) / ((1+r)**mesice_splaceni-1))
    celkova_suma = mesicni_splatka * mesice_splaceni
    celkovy_urok = celkova_suma - vypujcena_castka      # o kolik peněz částku přeplatim
    return mesicni_splatka, celkova_suma, r, mesice_splaceni, celkovy_urok

def mesicni_splatky(vypujcena_castka,mesicni_urok,mesice_splaceni):  # mesicni_splatky berou data z fce matika() a plivou list tuplů
    mesicni_platka, celkova_suma, r, mesice_splaceni, celkovy_urok = matika(vypujcena_castka,mesicni_urok,mesice_splaceni) # importuj hodnoty přes funkci matika a ulož je tam, kam chceš
    """Vygeneruj záznam ve formě:
     | Pořadí splátky | Částka z úroku | Jistina | Zbývá zaplatit |
    """             # tomuhle zápisu nerozumim
    splatky = []
    for mesic in range(1, mesice_splaceni+1):
        mesicni_urok = round(celkova_suma * r) # round zaokrouhluje
        splatky.append((mesic,mesicni_urok,round(mesicni_platka-mesicni_urok),round(celkova_suma)))
        celkova_suma = celkova_suma - mesicni_platka # pmt je mesicni_splatka
    return splatky

# GRAFIKA
def vytvor_hlavicku(vypujcena_castka,mesice_splaceni,castka_z_uroku,mesicni_splatka):
    return [["Vypůjčená částka: %d" % int(vypujcena_castka), "Splatím za: %d let" %int(mesice_splaceni/12),
             "Přeplatím o: %d" %castka_z_uroku, "Měsíční splátka: %d" %mesicni_splatka],
            ["Platba číslo","Úrok placený ve splátce","Jistina splacená ve splátce","Zbývá zaplatit"]]

# '|{:^{w1},}|{:^{w2},}|{:^{w3},}|{:^{w4},}|'

def sirka_sloupce(tabulka):             # u nich "column_widhts"
    pocet_sloupcu = len(tabulka[0])
    sirky_sloupcu = {}
    for sloupec_cislo in range (pocet_sloupcu):
        sloupec = ziskej_sloupec(sloupec_cislo, tabulka)
        sirka_sloupce_prom= len(max(sloupec, key=len)) + 4  # tomuhle nerozumim
        sirky_sloupcu["w%d" %(sloupec_cislo+1)] = sirka_sloupce_prom
    return sirky_sloupcu

def ziskej_sloupec(sloupec_cislo, tabulka):     # u nich to je "extract_column"
    sloupec = []
    for radek in tabulka:
        sloupec.append(str(radek[sloupec_cislo]))
    return sloupec

def formatuj_radky(data,vzor,sirky,formatovana_tabulka):
    for radek in data:
        line = vzor.format(*radek,**sirky)  # řádek k tisku
        formatovana_tabulka.append(line)       # nahrát do listu
    return formatovana_tabulka

def vloz_oddelovnik(tabulka, pocet_sloupcu, znacka = "="):
    sirka = len(max(tabulka, key = len))
    for sloupec in pocet_sloupcu:
        tabulka.insert(sloupec, znacka*sirka)
    return tabulka

def vytvor_tabulku(mesicni_splatky, hlavicka_vstupy):
    hlavicka = vytvor_hlavicku(*hlavicka_vstupy)
    tabulka = hlavicka + mesicni_splatky
    sirky = sirka_sloupce(tabulka)

    sablona_hlavicka = '|{:^{w1}}|{:^{w2}}|{:^{w3}}|{:^{w4}}|'
    sablona_data = '|{:^{w1},}|{:^{w2},}|{:^{w3},}|{:^{w4},}|'

    formatovana_tabulka = formatuj_radky(hlavicka,sablona_hlavicka,sirky,[])
    formatovana_tabulka = formatuj_radky(mesicni_splatky,sablona_data,sirky,formatovana_tabulka)
    formatovana_tabulka = vloz_oddelovnik(formatovana_tabulka,(1,3))

    return "\n".join(formatovana_tabulka)

def main():
    vypujcena_castka,mesicni_urok,mesice_splaceni = get_data()
    mesicni_splatka, celkova_suma, r, mesice_splaceni, celkovy_urok = matika(vypujcena_castka,mesicni_urok,mesice_splaceni)
    pmts = mesicni_splatky(vypujcena_castka,mesicni_urok,mesice_splaceni)
    # grafika
    hlavicka_vstupy = (vypujcena_castka,mesice_splaceni,celkovy_urok,mesicni_splatka)
    tabulka = vytvor_tabulku(pmts,hlavicka_vstupy)
    print(tabulka)
    file = open("C:\\Users\\Matěj\\Desktop\\hypoteka.txt","w")      # Interaguju s plochou... musim už mít tam založenej
    file.write(tabulka)                                             # tenhle soubor s timhle ménem... jinak se mi vytoří
                                                                    # tam, odkud pracuje můj skript
if __name__ == "__main__":
    main()

