import csv
from collections import Counter

# Configuration
FILE_PATH = 'RAW_met_lieux_inclusion_numerique - RAW_met_lieux_inclusion_numerique.csv'
LEVELS_PRIORITY = {'Expert': 3, 'Maîtrise': 2, 'Basique': 1, 'Non': 0}

def analyser_services():
    max_levels = []
    all_levels_found = []
    total_lieux = 0

    try:
        with open(FILE_PATH, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_lieux += 1
                service_str = row.get('niveau_service', '')
                if not service_str:
                    continue
                
                # Extraction des niveaux individuels (format: COMPETENCE/Niveau)
                parts = service_str.split(',')
                levels_in_row = []
                for p in parts:
                    if '/' in p:
                        try:
                            level = p.split('/')[1].strip()
                            if level in LEVELS_PRIORITY:
                                levels_in_row.append(level)
                                all_levels_found.append(level)
                        except IndexError:
                            continue
                
                if levels_in_row:
                    # Déterminer le meilleur niveau proposé par ce lieu
                    max_lvl = max(levels_in_row, key=lambda x: LEVELS_PRIORITY[x])
                    max_levels.append(max_lvl)

        # Affichage des résultats
        print(f"--- ANALYSE DE L'OFFRE NUMERIQUE (Sur {total_lieux} lieux) ---")
        
        print("\n1. RÉPARTITION PAR NIVEAU MAXIMUM PROPOSÉ PAR LIEU")
        counts_max = Counter(max_levels)
        for level in ['Expert', 'Maîtrise', 'Basique', 'Non']:
            count = counts_max.get(level, 0)
            percentage = (count / len(max_levels)) * 100 if max_levels else 0
            print(f"- {level}: {count} lieux ({percentage:.1f}%)")

        print("\n2. VOLUME TOTAL DES COMPÉTENCES (TOUTE LA MÉTROPOLE)")
        counts_all = Counter(all_levels_found)
        total_competences = len(all_levels_found)
        for level in ['Expert', 'Maîtrise', 'Basique', 'Non']:
            count = counts_all.get(level, 0)
            percentage = (count / total_competences) * 100 if total_competences else 0
            print(f"- {level}: {count} occurrences ({percentage:.1f}%)")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {FILE_PATH} est introuvable.")

if __name__ == "__main__":
    analyser_services()
