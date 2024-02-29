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
        return (pojisteny)


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
