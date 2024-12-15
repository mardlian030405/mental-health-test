# mental_health_checker.py

class MentalHealthChecker:
    def __init__(self):
        # Daftar gejala yang tersedia
        self.symptoms = {
            "G01": "Sering sakit kepala",
            "G02": "Tidak nafsu makan",
            "G03": "Sulit tidur",
            "G04": "Mudah takut",
            "G05": "Cemas atau khawatir",
            "G06": "Tangan gemetar",
            "G07": "Pencernaan terganggu",
            "G08": "Sulit berpikir jernih",
            "G09": "Merasa tidak bahagia",
            "G10": "Sering menangis",
            "G11": "Kesulitan menjalani aktivitas sehari-hari",
            "G12": "Sulit mengambil keputusan",
            "G13": "Pekerjaan sehari-hari terganggu",
            "G14": "Tidak mampu melakukan hal-hal bermanfaat",
            "G15": "Kehilangan minat pada berbagai hal",
            "G16": "Merasa tidak berharga",
            "G17": "Pikiran untuk mengakhiri hidup",
            "G18": "Merasa lelah sepanjang waktu",
            "G19": "Rasa tidak enak di perut",
            "G20": "Mudah lelah",
            "G21": "Kesulitan mengendalikan emosi",
            "G22": "Gangguan dalam berbicara",
        }

        # Aturan diagnosa berdasarkan gejala
        self.rules = {
            "P01": ["G01", "G05", "G08", "G11", "G12"],
            "P02": ["G03", "G05", "G07", "G14", "G18", "G19", "G20"],
            "P03": ["G03", "G04", "G08", "G09", "G11", "G12", "G13", "G14", "G15"],
            "P04": ["G02", "G03", "G05", "G08", "G09", "G14", "G15", "G16", "G17"],
            "P05": ["G02", "G03", "G05", "G09", "G11", "G12", "G13", "G14", "G15", "G16", "G17"],
            "P06": ["G01", "G02", "G05", "G08", "G09", "G11", "G15", "G16", "G20"],
            "P07": ["G04", "G05", "G07", "G08", "G16"],
            "P08": ["G21", "G22"],
            "P09": ["G01", "G02", "G04", "G05", "G08", "G09", "G12", "G15", "G17", "G21"],
        }

        # Nama penyakit berdasarkan kode
        self.diseases = {
            "P01": "Gangguan Mental Organik",
            "P02": "Gangguan Penggunaan NAPZA",
            "P03": "Skizofrenia dan Gangguan Psikotik Kronik Lain",
            "P04": "Gangguan Psikotik Akut",
            "P05": "Gangguan Bipolar",
            "P06": "Gangguan Depresi",
            "P07": "Gangguan Neurotik (Ansietas)",
            "P08": "Retardasi Mental",
            "P09": "Gangguan Kesehatan Jiwa Anak dan Remaja",
        }

    def get_symptoms(self):
        """Mengembalikan daftar gejala."""
        return self.symptoms

    def diagnose(self, symptoms):
        """
        Melakukan diagnosa berdasarkan gejala yang diberikan.
        :param symptoms: List kode gejala yang dipilih pengguna.
        :return: Nama penyakit yang terdeteksi atau pesan jika tidak ada diagnosa yang cocok.
        """
        for disease, required_symptoms in self.rules.items():
            if all(symptom in symptoms for symptom in required_symptoms):
                return self.diseases[disease]
        return "Tidak ada diagnosa yang sesuai. Silakan konsultasikan dengan ahli."
