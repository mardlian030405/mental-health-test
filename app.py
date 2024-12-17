from flask import Flask, render_template, request
from mental_health_checker import MentalHealthChecker
from dempster_shafer import dempster_shafer

app = Flask(__name__)
checker = MentalHealthChecker()

symptoms = {
    "G01": "Sering sakit kepala",
    "G02": "Tidak nafsu makan",
    "G03": "Sulit tidur",
    "G04": "Mudah takut",
    "G05": "Cemas atau khawatir",
    "G07": "Pencernaan terganggu",
    "G08": "Sulit berpikir jernih",
    "G09": "Merasa tidak bahagia",
    "G11": "Kesulitan menjalani aktivitas sehari-hari",
    "G12": "Sulit mengambil keputusan",
}

# Route untuk halaman utama (input gejala)
@app.route("/dempster", methods=["GET", "POST"])
def dempster():
    if request.method == "POST":
        selected_symptoms = request.form.getlist("gejala")
        results = dempster_shafer(selected_symptoms)
        return render_template("hasil.html", results=results)
    return render_template("dempster.html", symptoms=symptoms)

# Rute untuk halaman utama
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/symthoms")
def sympthoms():
    return render_template("symthoms.html")

# Rute untuk halaman konsultasi
@app.route("/consultation", methods=["GET", "POST"])
def consultation():
    if request.method == "POST":
        # Ambil gejala yang dipilih pengguna dari form
        symptoms = request.form.getlist("symptoms")
        # Lakukan diagnosa berdasarkan gejala
        result = checker.diagnose(symptoms)
        # Tampilkan hasil diagnosa
        return render_template("result.html", result=result)
    # Ambil daftar gejala untuk ditampilkan di form
    symptoms = checker.get_symptoms()
    return render_template("consultation.html", symptoms=symptoms)

# Jalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)
