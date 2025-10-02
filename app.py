<<<<<<< HEAD
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/question')
def question():
    return render_template("question.html")

@app.route('/result')
def result():
    # Di sini nanti bisa ditambahkan logika untuk menentukan hasil
    # Untuk contoh sederhana kita tampilkan hasil statis
    rekomendasi = "Ekstrakurikuler Paduan Suara 🎤"
    return render_template("result.html", rekomendasi=rekomendasi)

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/question')
def question():
    return render_template("question.html")

@app.route('/result')
def result():
    # Di sini nanti bisa ditambahkan logika untuk menentukan hasil
    # Untuk contoh sederhana kita tampilkan hasil statis
    rekomendasi = "Ekstrakurikuler Paduan Suara 🎤"
    return render_template("result.html", rekomendasi=rekomendasi)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 3a13328fd7355d5a1f9f90dce436b8a178f15d77
