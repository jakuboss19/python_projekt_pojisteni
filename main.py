class Pojisteni:
    def __init__(self):
        self.pojisteni = []

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = {
            "jmeno": jmeno,
            "prijmeni": prijmeni,
            "vek": vek,
            "telefon": telefon
        }
        self.pojisteni.append(pojisteny)

    def zobraz_seznam(self):
        for pojisteny in self.pojisteni:
            return(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny['jmeno'] == jmeno and pojisteny['prijmeni'] == prijmeni:
                return pojisteny
        return None

    def __str__(self):
        seznam = ""
        for pojisteny in self.pojisteni:
            seznam += f"Jméno: {pojisteny['jmeno']}, Příjmení: {pojisteny['prijmeni']}, Věk: {pojisteny['vek']}, Telefon: {pojisteny['telefon']}\n"
        return seznam.strip()

# Třída uživatelského rozhraní
class SpravaPojisteni:
    def __init__(self):
        self.pojisteni = Pojisteni()

    # Metoda vytvoří a ověřuje vstupní data pojištěného
    def vytvor_pojisteneho(self):
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        vek = input("Věk: ")
        telefon = input("Telefon: ")

        if not jmeno or not prijmeni or not vek or not telefon:
            print("Jméno, příjmení, věk a telefon jsou povinná pole!")

        elif not jmeno.isalpha() or not prijmeni.isalpha():
            print("Jméno a příjmení musí být písmena!")

        elif not vek.isdigit() or not telefon.isdigit():
            print("Věk a telefon musí být čísla!")

        else:
            self.pojisteni.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
            print("Pojištěný byl vytvořen.")

    # Metoda vyprintuje do konzole vytvořený seznam pojištěnců
    def zobraz_seznam_pojisteni(self):
        print(self.pojisteni)

    # Metoda vyhledá pojištěného podle jména a příjmení
    def najdi_pojisteneho(self):
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        nalezeny = self.pojisteni.najdi_pojisteneho(jmeno, prijmeni)
        if nalezeny:
            print(nalezeny)
        else:
            print("Pojištěný nebyl nalezen.")

    # Cyklus while True na kterém běží uživatelské rozhraní
    def spust(self):
        while True:
            print("\n----- EVIDENCE POJISTENYCH -----")
            print("1. Vytvořit pojištěného")
            print("2. Zobrazit seznam pojištěných")
            print("3. Najít pojištěného")
            print("4. Konec")

            volba = input("Vyberte možnost: ")

            if volba == "1":
                self.vytvor_pojisteneho()

            elif volba == "2":
                self.zobraz_seznam_pojisteni()

            elif volba == "3":
                self.najdi_pojisteneho()

            elif volba == "4":
                print("Děkujeme za použití naší aplikace")
                break

            else:
                print("Neplatná volba. Zadejte číslo od 1 do 4.")

# Spuštění aplikace
sprava_pojisteni = SpravaPojisteni()
sprava_pojisteni.spust()
