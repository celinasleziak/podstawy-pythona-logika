# ==========================================================
# MOJE PORTFOLIO: PODSTAWY LOGIKI I FUNKCJI W PYTHONIE
# Autor: [Twoje Imię/Nick]
# ==========================================================

# --- ZADANIE 1: SYMULACJA KOSZYKA ALLEGRO SMART ---
# Sprawdza, czy dany produkt kwalifikuje się do darmowej dostawy.
koszyk = [
    {"przedmiot": "Myszka", "cena": 35, "super_sprzedawca": True},
    {"przedmiot": "Klawiatura", "cena": 120, "super_sprzedawca": False},
    {"przedmiot": "Podkładka", "cena": 45, "super_sprzedawca": True},
    {"przedmiot": "Głośnik", "cena": 200, "super_sprzedawca": True}
]

def czy_smart(cena, status):
    if cena >= 40 and status == True:
        return True
    return False

print("--- ANALIZA KOSZYKA ---")
for produkt in koszyk:
    if czy_smart(produkt["cena"], produkt["super_sprzedawca"]):
        print(f"{produkt['przedmiot']} - DOSTAWA ZA DARMO.")
    else:
        print(f"{produkt['przedmiot']} - placisz 15zl za dostawe")


# --- ZADANIE 2: SYSTEM RABATOWY ---
def oblicz_finalna_cene(wydana_kwota):
    if wydana_kwota > 500:
        return wydana_kwota - 50
    return wydana_kwota

# ile_wydal = int(input("podaj wydana kwote: "))
# print(f"Do zapłaty: {oblicz_finalna_cene(ile_wydal)}")


# --- ZADANIE 3: NAPIWEK W RESTAURACJI ---
def dolicz_napiwek(rachunek):
    if rachunek > 100:
        return rachunek * 1.15
    return rachunek

# kwota = int(input("wpisz kwote rachunku: "))
# print(f"Laczna cena z napiwkiem: {dolicz_napiwek(kwota)}")


# --- ZADANIE 4: BRAMKA VIP ---
def czy_moze_wejsc(wiek, czy_vip):
    if czy_vip == "tak" or wiek >= 18:
        return True 
    return False 

# w = int(input("podaj wiek: "))
# v = input("czy masz wejscie vip?: ")
# print("Zapraszamy!" if czy_moze_wejsc(w, v) else "Wstep wzbroniony")


# --- ZADANIE 5: BILETY STUDENCKIE I BACKSTAGE ---
def oblicz_cene(czy_student):
    return 50 if czy_student == "tak" else 100

def czy_backstage(wiek):
    return True if wiek <= 21 else False

# s = input("czy masz legitymacje? (tak/nie): ")
# age = int(input("podaj wiek: "))
# print(f"Cena: {oblicz_cene(s)}, Backstage: {czy_backstage(age)}")


# --- ZADANIE 6: LOTNISKO (CENY I BAGAŻ) ---
def oblicz_znizke(wiek):
    return 100 if wiek < 12 else 250

def czy_nadbagaz(waga):
    return waga > 20

# age = int(input("Wiek: "))
# weight = float(input("Waga bagazu: "))
# print(f"Cena biletu: {oblicz_znizke(age)}, Nadbagaz: {czy_nadbagaz(weight)}")


# --- ZADANIE 7: WYCIĄG NARCIARSKI (FINAŁ) ---
def cena_karnetu(wiek):
    if wiek < 16: return 80
    elif 16 <= wiek <= 65: return 150
    else: return 100

def czy_bezpieczny(wiatr):
    return wiatr <= 50

# wiatr = int(input("Wiatr (km/h): "))
# if czy_bezpieczny(wiatr):
#     wiek = int(input("Wiek: "))
#     print(f"Cena karnetu: {cena_karnetu(wiek)}zl")
# else:
#     print("Wyciag zamkniety!")


# ==========================================================
# ZADANIE: SYSTEM ZARZĄDZANIA KINEM (FILTROWANIE DANYCH)
# Cel: Prezentacja zagnieżdżonej logiki i iteracji po obiektach
# ==========================================================

filmy = [
    {"tytul": "Król Lew", "wiek": 7, "3d": False},
    {"tytul": "Batman", "wiek": 16, "3d": True},
    {"tytul": "Piła", "wiek": 18, "3d": False},
    {"tytul": "Toy Story", "wiek": 3, "3d": True},
    {"tytul": "Diuna", "wiek": 12, "3d": True}
]

def czy_moze_obejrzec(wiek_widza, wiek_filmu):
    """Sprawdza, czy wiek widza pozwala na obejrzenie danego tytułu."""
    if wiek_widza >= wiek_filmu:
        return True
    else:
        return False 

# --- PRZYKŁAD DZIAŁANIA DLA WIEKU 14 LAT ---
# moj_wiek = int(input("ile masz lat? "))  <-- Odkomentuj, aby użyć interaktywnie
moj_wiek = 14 

print(f"--- RAPORT KINOWY DLA WIEKU: {moj_wiek} ---")

for film in filmy:
    # 1. Sprawdzamy dostępność na podstawie wieku
    if czy_moze_obejrzec(moj_wiek, film["wiek"]):
        
        # 2. Sprawdzamy dodatkowy atrybut (3D)
        if film["3d"] == True:
            print(f"{film['tytul']} - Zapraszamy na seans! (Zabierz okulary 3D! 🕶️)")
        else:
            print(f"{film['tytul']} - Zapraszamy na seans!")
            
    else:
        # 3. Jeśli wiek jest niewystarczający
        print(f"{film['tytul']} - Jesteś za młody na ten film. ❌")

print("-" * 40)
