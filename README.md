# **Sistem Pakar Rekomendasi Ekstrakurikuler**
Sistem ini merupakan sistem pakar berbasis web yang dibangun menggunakan framework Flask (Python). 
Tujuannya sistem ini adalah untuk memberikan rekomendasi kegiatan ekstrakurikuler yang paling sesuai dengan minat dan karakter siswa berdasarkan pertanyaan sederhana.

**Deskripsi Singkat**
Aplikasi ini menggunakan pendekatan _rule-based Expert system_, ini dirancang untuk membantu siswa menentukan kegiatan ekstrakurikuler yang paling sesuai dengan minat, kemampuan, serta karakteristik pribadinya. Sistem ini meniru cara berpikir seorang konselor atau guru pembimbing dengan menggunakan pendekatan, dimana keputusan akhir ditentukan melalui sekumpulan aturan logika (_if–then rules_) berdasarkan jawaban siswa terhadap serangkaian pertanyaan. Setiap pertanyaan mewakili aspek tertentu dari kepribadian, kebiasaan, dan kemampuan fisik pengguna, seperti kemampuan bekerja sama, daya ingat, kedisiplinan, serta ketahanan mental dan fisik. Setelah pengguna menjawab seluruh pertanyaan, sistem akan menganalisis pola jawaban tersebut untuk memberikan rekomendasi kegiatan ekstrakurikuler yang paling cocok.

- Seni Musik
- Seni Tari
- Pencak Silat
- Futsal
- Pramuka
- Paskibra

# **Teknologi yang Digunakan**

- Python 3.x
- Flask– Web framework untuk routing dan session handling
- HTML5, CSS3– Tampilan front-end
- Jinja2 Template Engine– Integrasi data dari Python ke HTML

# **Alur Sistem**

- index.html– Halaman pembuka yang menjelaskan tujuan aplikasi dan menyediakan tombol Mulai Konsultasi.
- question.html– Menampilkan daftar pertanyaan yang harus dijawab pengguna satu per satu dengan pilihan “Ya” atau “Tidak”.
- save_answer (Flask Route)– Menyimpan setiap jawaban ke dalam session Flask.
- result.html– Setelah seluruh pertanyaan dijawab, sistem akan memproses seluruh jawaban dan menampilkan hasil akhir berupa rekomendasi ekstrakurikuler.

# **Mekanisme Penalaran (_Rule-Based System_)**
Fungsi utama sistem pakar ini adalah get_result(answers) yang berisi sejumlah aturan (rules).
Contoh aturan:
<pre> if (answers[0] == "Ya" and
    answers[1] == "Ya" and
    answers[2] == "Ya" and
    answers[6] == "Ya"):
    return "A01 - Seni Musik" </pre>
Setiap aturan merepresentasikan kombinasi jawaban “Ya” yang menunjukkan kecenderungan minat terhadap suatu bidang ekstrakurikuler. Jika tidak ada aturan yang cocok, sistem akan menampilkan pesan:
**"Tidak ditemukan rekomendasi yang cocok berdasarkan jawaban Anda."**
<img width="1050" height="433" alt="image" src="https://github.com/user-attachments/assets/94e558e4-bf4e-473d-a478-d10a881e6fae" />

**Desain Halaman**
1. index.html
   Berisi halaman sambutan dengan deskripsi singkat sistem pakar dan tombol “Mulai Konsultasi” yang mengarahkan ke /question.
2. question.html
   Menampilkan daftar pertanyaan dengan dua tombol jawaban — Ya dan Tidak. Setiap jawaban dikirim ke server menggunakan POST agar tersimpan dalam session Flask.
3. result.html
   Menampilkan hasil akhir rekomendasi ekstrakurikuler berdasarkan evaluasi dari seluruh jawaban.
4. style.css
   Mengatur tampilan visual seluruh halaman (warna, tata letak, tombol, dan tipografi) agar antarmuka terlihat menarik dan responsif.

# **Input:**
Ya, Ya, Ya, Ya, Tidak, Ya, Ya, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak
Output:
**"Rekomendasi Ekstrakurikuler Anda: A01 - Seni Musik"**
<img width="1107" height="482" alt="image" src="https://github.com/user-attachments/assets/ca4af130-f9f5-4560-8558-a6b987e25a37" />

# **Contoh Tampilan Output**
<img width="1348" height="692" alt="image" src="https://github.com/user-attachments/assets/fccc0ae8-2cc4-47f6-8ecd-20025b6f610f" />
<img width="796" height="691" alt="image" src="https://github.com/user-attachments/assets/66fe02c4-cf5d-4163-a376-827a0d6cf130" />

# **Tim Pengembang**

Dibuat dengan menggunakan Flask oleh [KELOMPOK 7 (ExPro Team)].
Project ini merupakan implementasi sederhana dari sistem pakar berbasis aturan (rule-based expert system) untuk memenuhi tugas sebelum UTS mata kuliah KECERDASAN BUATAN.
