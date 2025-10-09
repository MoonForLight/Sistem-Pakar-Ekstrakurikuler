from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "ekstra123"

# daftar pertanyaan
questions = [
    "Apakah kamu suka bernyanyi?",
    "Apakah kamu suka bermain musik?",
    "Apakah kamu memiliki konsentrasi dan ingatan yang kuat?",
    "Apakah kamu mempunyai fisik yang sehat?",
    "Apakah kamu suka menirukan gerakan tubuh?",
    "Apakah kamu suka bekerja sama dalam tim?",
    "Apakah kamu menyukai bela diri?",
    "Apakah kamu memiliki jiwa pantang menyerah?",
    "Apakah kamu mempunyai mental yang kuat?",
    "Apakah kamu suka bermain futsal atau bola?",
    "Apakah kamu memiliki karakter disiplin?",
    "Apakah kamu memiliki berat badan ideal?",
    "Apakah kamu memiliki jiwa kejujuran?",
    "Apakah kamu tidak mudah takut akan sikap tegas?",
    "Apakah kamu memiliki jiwa kepemimpinan?",
    "Apakah kamu memiliki rasa bertanggung jawab?",
    "Apakah kamu mempunyai tinggi badan ideal?",
    "Apakah kamu mempunyai postur tegap?",
    "Apakah kamu mampu melakukan PBB (Peraturan Baris Berbaris)?",
    "Apakah kamu suka menari?"
]

# fungsi untuk menentukan hasil


def get_result(answers):
    # Urutan answers sama dengan urutan questions (index 0 = jawaban pertanyaan ke-1, dst.)

    # Rule 1: Seni Musik [cite: 150]
    if (answers[0] == "Ya" and   # B01: Suka bernyanyi
        answers[1] == "Ya" and   # B02: Suka bermain musik
        answers[2] == "Ya" and   # B03: Konsentrasi dan ingatan kuat
            answers[6] == "Ya"):     # B07: Suka bekerja sama dalam tim
        return "A01 - Seni Musik"

    # Rule 2: Seni Tari [cite: 151]
    if (answers[4] == "Ya" and   # B05: Suka menari
        answers[5] == "Ya" and   # B06: Suka meniru gerakan tubuh
        answers[2] == "Ya" and   # B03: Konsentrasi dan ingatan kuat
        answers[3] == "Ya" and   # B04: Fisik sehat
        answers[6] == "Ya" and   # B07: Suka bekerja sama dalam tim
            answers[12] == "Ya"):    # B13: Berat ideal
        return "A02 - Seni Tari"

    # Rule 3: Pencak Silat [cite: 152]
    if (answers[7] == "Ya" and   # B08: Suka bela diri
        answers[8] == "Ya" and   # B09: Pantang menyerah
        answers[9] == "Ya" and   # B10: Mental kuat
        answers[3] == "Ya" and   # B04: Fisik sehat
            answers[6] == "Ya"):     # B07: Suka bekerja sama dalam tim
        return "A03 - Pencak Silat"

    # Rule 4: Futsal [cite: 153]
    if (answers[10] == "Ya" and  # B11: Suka futsal/bola
        answers[8] == "Ya" and   # B09: Pantang menyerah
        answers[11] == "Ya" and  # B12: Disiplin
        answers[9] == "Ya" and   # B10: Mental kuat
        answers[3] == "Ya" and   # B04: Fisik sehat
        answers[6] == "Ya" and   # B07: Suka bekerja sama dalam tim
            answers[12] == "Ya"):    # B13: Berat ideal
        return "A04 - Futsal"

    # Rule 5: Pramuka [cite: 154]
    if (answers[13] == "Ya" and  # B14: Jujur
        answers[14] == "Ya" and  # B15: Tidak takut alam
        answers[15] == "Ya" and  # B16: Jiwa kepemimpinan
        answers[8] == "Ya" and   # B09: Pantang menyerah
        answers[16] == "Ya" and  # B17: Bertanggung jawab
        answers[11] == "Ya" and  # B12: Disiplin
        answers[9] == "Ya" and   # B10: Mental kuat
        answers[3] == "Ya" and   # B04: Fisik sehat
            answers[6] == "Ya"):     # B07: Suka bekerja sama dalam tim
        return "A05 - Pramuka"

    # Rule 6: Paskibra [cite: 155]
    if (answers[17] == "Ya" and  # B18: Tinggi ideal
        answers[18] == "Ya" and  # B19: Postur tegap
        answers[19] == "Ya" and  # B20: Mampu PBB
        answers[12] == "Ya" and  # B13: Berat ideal
        answers[8] == "Ya" and   # B09: Pantang menyerah
        answers[11] == "Ya" and  # B12: Disiplin
        answers[9] == "Ya" and   # B10: Mental kuat
        answers[3] == "Ya" and   # B04: Fisik sehat
            answers[6] == "Ya"):     # B07: Suka bekerja sama dalam tim
        return "A06 - Paskibra"

    # Jika tidak ada aturan yang cocok
    return "Tidak ditemukan rekomendasi yang cocok berdasarkan jawaban Anda."


@app.route("/")
def index():
    session["answers"] = []  # reset jawaban
    print("[DEBUG] Reset jawaban user")
    return render_template("index.html")


@app.route("/question")
def question():
    print("[DEBUG] Mulai konsultasi. Total pertanyaan:", len(questions))
    return render_template("question.html", questions=questions)


@app.route("/save_answer", methods=["POST"])
def save_answer():
    answer = request.form.get("answer")
    if "answers" not in session:
        session["answers"] = []

    # ambil list lama, tambahkan jawaban baru, simpan ulang
    answers = session["answers"]
    answers.append(answer)
    session["answers"] = answers

    print(f"[DEBUG] Jawaban ke-{len(answers)} tersimpan: {answer}")
    print("[DEBUG] Semua jawaban sementara:", session["answers"])

    if len(session["answers"]) >= len(questions):
        return redirect(url_for("result"))
    return "", 204


@app.route("/result")
def result():
    answers = session.get("answers", [])
    print("[DEBUG] Jawaban final user:", answers)

    final_result = get_result(answers) if answers else "Belum ada hasil"
    print("[DEBUG] Hasil akhir:", final_result)

    return render_template("result.html", result=final_result, answers=answers)


if __name__ == "__main__":
    app.run(debug=True)
