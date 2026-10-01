import time
import sys

def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def game_loop():
    # Startstatistieken van jouw bedrijf
    bedrijfsnaam = input("Wat is de naam van jouw bedrijf? ")
    geld = 50000
    gebouwen = {"Kleine Kantoorruimte": 1}
    autos = {}
    inkomen_per_seconde = 10
    
    # Prijzenlijst van de markt
    markt_gebouwen = {
        "Magazijn": 25000,
        "Hoofdkantoor": 100000,
        "Fabriek": 250000
    }
    
    markt_autos = {
        "Bestelbus": 15000,
        "Vrachtwagen": 45000,
        "Directie Tesla": 80000
    }

    while True:
        print("\n" + "="*40)
        type_text(f"--- {bedrijfsnaam.upper()} DASHBOARD ---")
        print(f"Saldo: €{geld:,}")
        print(f"Inkomsten: +€{inkomen_per_seconde}/sec")
        print(f"Gebouwen: {gebouwen}")
        print(f"Voertuigen: {autos if autos else 'Geen'}")
        print("="*40)
        
        print("\nWat wil je doen?")
        print("1. Werken (Genereer direct €5.000)")
        print("2. Investeren in Gebouwen")
        print("3. Voertuigen Kopen")
        print("4. Wachten (Laat passief inkomen binnenkomen)")
        print("5. Spel afsluiten")
        
        keuze = input("\nMaak een keuze (1-5): ")
        
        if keuze == "1":
            geld += 5000
            type_text("\n[!] Je hebt hard gewerkt en €5.000 verdiend!")
            
        elif keuze == "2":
            print("\n--- GEBOUWEN MARKT ---")
            for i, (gebouw, prijs) in enumerate(markt_gebouwen.items(), 1):
                print(f"{i}. {gebouw} - €{prijs:,}")
            print("4. Terug")
            
            g_keuze = input("Welk gebouw wil je kopen? (1-4): ")
            lijst_gebouwen = list(markt_gebouwen.keys())
            
            if g_keuze in ["1", "2", "3"]:
                gekozen_gebouw = lijst_gebouwen[int(g_keuze)-1]
                prijs = markt_gebouwen[gekozen_gebouw]
                
                if geld >= prijs:
                    geld -= prijs
                    gebouwen[gekozen_gebouw] = gebouwen.get(gekozen_gebouw, 0) + 1
                    # Elk gebouw verhoogt passief inkomen
                    extra_inkomen = int(prijs * 0.05)
                    inkomen_per_seconde += extra_inkomen
                    type_text(f"\n[V] Succes! Je hebt een {gekozen_gebouw} gekocht. Je passieve inkomen stijgt met €{extra_inkomen}/sec!")
                else:
                    type_text("\n[X] Onvoldoende saldo voor deze investering.")
                    
        elif keuze == "3":
            print("\n--- VOERTUIGEN MARKT ---")
            for i, (auto, prijs) in enumerate(markt_autos.items(), 1):
                print(f"{i}. {auto} - €{prijs:,}")
            print("4. Terug")
            
            a_keuze = input("Welke auto wil je kopen? (1-4): ")
            lijst_autos = list(markt_autos.keys())
            
            if a_keuze in ["1", "2", "3"]:
                gekozen_auto = lijst_autos[int(a_keuze)-1]
                prijs = markt_autos[gekozen_auto]
                
                if geld >= prijs:
                    geld -= prijs
                    autos[gekozen_auto] = autos.get(gekozen_auto, 0) + 1
                    # Auto's geven een directe boost aan werk-inkomsten of passief inkomen
                    extra_inkomen = int(prijs * 0.08)
                    inkomen_per_seconde += extra_inkomen
                    type_text(f"\n[V] Prachtig! Je hebt een {gekozen_auto} toegevoegd aan je wagenpark. +€{extra_inkomen}/sec!")
                else:
                    type_text("\n[X] Onvoldoende saldo voor dit voertuig.")
                    
        elif keuze == "4":
            type_text("\n[..] Tijd tikt door... Je bedrijf draait op de achtergrond.")
            time.sleep(2) # Simuleer 5 seconden aan inkomsten
            verdiend = inkomen_per_seconde * 5
            geld += verdiend
            type_text(f"[+] Je hebt €{verdiend:,} aan passief inkomen ontvangen!")
            
        elif keuze == "5":
            type_text("\nBedankt voor het spelen! Je bedrijf is opgeslagen in het geheugen.")
            break
        else:
            print("\n[!] Ongeldige keuze, probeer het opnieuw.")

if __name__ == "__main__":
    print("Welkom bij Business Tycoon Simulator!")
    game_loop()
