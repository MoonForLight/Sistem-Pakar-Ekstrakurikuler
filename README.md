# **Sistem Pakar Rekomendasi Ekstrakurikuler**
Sistem ini merupakan sistem pakar berbasis web yang dibangun menggunakan framework Flask (Python). 
Tujuannya sistem ini adalah untuk memberikan rekomendasi kegiatan ekstrakurikuler yang paling sesuai dengan minat dan karakter siswa berdasarkan pertanyaan sederhana.

# **Deskripsi Singkat**
Aplikasi ini menggunakan pendekatan _rule-based Expert system_, ini dirancang untuk membantu siswa menentukan kegiatan ekstrakurikuler yang paling sesuai dengan minat, kemampuan, serta karakteristik pribadinya. Sistem ini meniru cara berpikir seorang konselor atau guru pembimbing dengan menggunakan pendekatan, dimana keputusan akhir ditentukan melalui sekumpulan aturan logika (_if–then rules_) berdasarkan jawaban siswa terhadap serangkaian pertanyaan. Setiap pertanyaan mewakili aspek tertentu dari kepribadian, kebiasaan, dan kemampuan fisik pengguna, seperti kemampuan bekerja sama, daya ingat, kedisiplinan, serta ketahanan mental dan fisik. Setelah pengguna menjawab seluruh pertanyaan, sistem akan menganalisis pola jawaban tersebut untuk memberikan rekomendasi kegiatan ekstrakurikuler yang paling cocok.

- **Seni Musik**
- **Seni Tari**
- **Pencak Silat**
- **Futsal**
- **Pramuka**
- **Paskibra**

# **Teknologi yang Digunakan**

- **Python 3.x**
- **Flask– Web framework untuk routing dan session handling**
- **HTML5, CSS3– Tampilan front-end**
- **Jinja2 Template Engine– Integrasi data dari Python ke HTML**
  
# **Alur Sistem**

- **index.html**– Halaman pembuka yang menjelaskan tujuan aplikasi dan menyediakan tombol Mulai Konsultasi.
- **question.html**– Menampilkan daftar pertanyaan yang harus dijawab pengguna satu per satu dengan pilihan “Ya” atau “Tidak”.
- **save_answer (Flask Route)**– Menyimpan setiap jawaban ke dalam session Flask.
- **result.html**– Setelah seluruh pertanyaan dijawab, sistem akan memproses seluruh jawaban dan menampilkan hasil akhir berupa rekomendasi ekstrakurikuler.

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
<img width="1770" height="964" alt="image" src="https://github.com/user-attachments/assets/e022890d-6751-4e46-941b-594ab667c5c6" />


# **Desain Halaman**
1. **index.html**
   Berisi halaman sambutan dengan deskripsi singkat sistem pakar dan tombol “Mulai Konsultasi” yang mengarahkan ke /question.
2. **question.html**
   Menampilkan daftar pertanyaan dengan dua tombol jawaban — Ya dan Tidak. Setiap jawaban dikirim ke server menggunakan POST agar tersimpan dalam session Flask.
3. **result.html**
   Menampilkan hasil akhir rekomendasi ekstrakurikuler berdasarkan evaluasi dari seluruh jawaban.
4. **style.css**
   Mengatur tampilan visual seluruh halaman (warna, tata letak, tombol, dan tipografi) agar antarmuka terlihat menarik dan responsif.

# **Input:**
Ya, Ya, Ya, Ya, Tidak, Ya, Ya, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak, Tidak
Output:
**"Rekomendasi Ekstrakurikuler Anda: A01 - Seni Musik"**
<img width="1733" height="951" alt="image" src="https://github.com/user-attachments/assets/f036240b-42ee-4c64-bfa3-20a35eb180c6" />

# **Contoh Tampilan Output**
<img width="1766" height="976" alt="image" src="https://github.com/user-attachments/assets/dae69571-5b29-4b49-a4ce-96c82e68c4cc" />
<img width="1773" height="966" alt="image" src="https://github.com/user-attachments/assets/545227d6-51ef-4cf7-9be5-c93aa868cd04" />
<img width="1733" height="965" alt="image" src="https://github.com/user-attachments/assets/a97b8c99-75ef-4b70-981c-a737bcefef04" />


# **Tim Pengembang**

Dibuat dengan menggunakan Flask oleh [KELOMPOK 7 (ExPro Team)].
Project ini merupakan implementasi sederhana dari sistem pakar berbasis aturan (rule-based expert system) untuk memenuhi tugas sebelum UTS mata kuliah KECERDASAN BUATAN.
