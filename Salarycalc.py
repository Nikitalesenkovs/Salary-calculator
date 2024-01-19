def calculate_income_tax(alga):
    # Pieņemsim fiksēto nodokļa likmi kā piemēru
    nodokļa_likme = 0.21
    standarta_nodoklis = 500.0  # Standarta atlīdzība

    # Aprēķina ienākuma nodokli
    nodoklis = max((alga - standarta_nodoklis) * nodokļa_likme, 0)
    return nodoklis

def calculate_social_contributions(alga):
    # Pieņemsim fiksēto procentu sociālajiem ieguldījumiem kā piemēru
    sociālie_ieguldījumi_procents = 0.1
    return alga * sociālie_ieguldījumi_procents

def main():
    print("Nodokļu kalkulators (Latvija)")
    alga = float(input("Ievadiet savu algu: "))

    # Aprēķina nodokļus
    ienākuma_nodoklis = calculate_income_tax(alga)
    sociālie_ieguldījumi = calculate_social_contributions(alga)
    kopējais_nodoklis = ienākuma_nodoklis + sociālie_ieguldījumi

    # Parāda rezultātus
    print("\nRezultāti:")
    print(f"Alga: €{alga}")
    print(f"Ieņēmuma nodoklis: €{ienākuma_nodoklis}")
    print(f"Sociālie ieguldījumi: €{sociālie_ieguldījumi}")
    print(f"Kopējais nodoklis: €{kopējais_nodoklis}")
    print(f"Tīrā alga: €{alga - kopējais_nodoklis}")

# Izsauc funkciju main() tieši
main()