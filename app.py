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
    score = {
        "A01 - Seni Musik": 0,
        "A02 - Seni Tari": 0,
        "A03 - Pencak Silat": 0,
        "A04 - Futsal": 0,
        "A05 - Pramuka": 0,
        "A06 - Paskibra": 0
    }

    if len(answers) >= 20:   # biar aman
        if answers[0] == "Ya" or answers[1] == "Ya":
            score["A01 - Seni Musik"] += 2
        if answers[4] == "Ya" or answers[19] == "Ya":
            score["A02 - Seni Tari"] += 2
        if answers[6] == "Ya" or answers[7] == "Ya":
            score["A03 - Pencak Silat"] += 2
        if answers[9] == "Ya":
            score["A04 - Futsal"] += 2
        if answers[5] == "Ya" or answers[15] == "Ya":
            score["A05 - Pramuka"] += 2
        if answers[11] == "Ya" or answers[17] == "Ya" or answers[18] == "Ya":
            score["A06 - Paskibra"] += 2

    best = max(score, key=score.get)
    if score[best] == 0:
        return "Belum ada hasil"
    return best


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
