# app.py
from flask import Flask, render_template, request
from mental_health_checker import MentalHealthChecker

# Inisialisasi aplikasi Flask
app = Flask(__name__)
checker = MentalHealthChecker()

# Rute untuk halaman utama
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

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
