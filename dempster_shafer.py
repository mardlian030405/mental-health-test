from collections import defaultdict

# Basis pengetahuan probabilitas untuk gejala (masses dalam Dempster-Shafer)
knowledge_base = {
    "Gangguan Mental Organik": {"G01": 0.6, "G05": 0.7, "G08": 0.8, "G11": 0.9, "G12": 0.6},  # Gangguan Mental Organik
    "NAPZA": {"G03": 0.6, "G05": 0.7, "G07": 0.5, "G14": 0.8, "G18": 0.7, "G19": 0.6, "G20": 0.6},  # NAPZA
    "Skizofrenia": {"G03": 0.7, "G04": 0.8, "G08": 0.7, "G09": 0.8, "G11": 0.7, "G12": 0.6, "G13": 0.6},  # Skizofrenia
    "Psikotik Akut": {"G02": 0.6, "G03": 0.6, "G05": 0.7, "G08": 0.8, "G09": 0.7, "G14": 0.8, "G15": 0.7},  # Psikotik Akut
    "Bipolar": {"G02": 0.7, "G03": 0.8, "G05": 0.8, "G09": 0.7, "G11": 0.8, "G12": 0.7, "G14": 0.8},  # Bipolar
}

# Fungsi Dempster-Shafer
def dempster_shafer(selected_symptoms):
    results = defaultdict(float)

    for penyakit, gejala_dict in knowledge_base.items():
        mass = 1.0  # Initialize mass to 1 for combination
        for gejala in selected_symptoms:
            if gejala in gejala_dict:
                mass *= gejala_dict[gejala]  # Combine evidence

        if mass > 0:
            results[penyakit] = mass

    # Normalize results
    total_mass = sum(results.values())
    for key in results:
        results[key] = results[key] / total_mass if total_mass > 0 else 0

    return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
