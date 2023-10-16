**Readme File**

**Nama Projek:** Sentiment Analisis dari Kolom Komentar Video Trailer The Nun 2 Menggunakan Metode LSTM

**Kelompok:**
* Alem Ardemi
* Bintang Annisa Maharani
* Fabio Hedfam G. Siregar

**Deskripsi:**

Proyek ini bertujuan untuk melakukan sentiment analisis dari kolom komentar video trailer The Nun 2 menggunakan metode LSTM. Sentiment analisis adalah proses mengidentifikasi emosi atau sentimen yang terkandung dalam teks. Dalam proyek ini, sentimen yang diidentifikasi adalah positif, negatif, dan netral.

**Metode:**

Metode yang digunakan dalam proyek ini adalah metode LSTM (Long Short-Term Memory). LSTM adalah model jaringan saraf tiruan yang dapat mempelajari pola temporal dalam data. Dalam proyek ini, LSTM digunakan untuk mempelajari pola temporal dari sentimen yang terkandung dalam komentar video trailer The Nun 2.

**Data:**

Data yang digunakan dalam proyek ini adalah kolom komentar video trailer The Nun 2 yang diambil dari YouTube sebanyak 2000 komentar. Data tersebut dibersihkan terlebih dahulu untuk menghilangkan komentar yang tidak relevan.

**Hasil:**

Hasil dari proyek ini adalah model LSTM yang dapat memprediksi sentimen dari komentar video trailer The Nun 2 dengan akurasi sementara 66%.


**Instalasi**

Untuk menjalankan proyek ini, diperlukan beberapa library Python, yaitu:

* numpy
* pandas
* keras
* tensorflow

Untuk menginstal library-library tersebut, dapat menggunakan perintah berikut:

```
pip install numpy pandas keras tensorflow
```

**Pemrosesan Data**

Data yang digunakan dalam proyek ini adalah kolom komentar video trailer The Nun 2 yang diambil dari YouTube. Data tersebut dibersihkan terlebih dahulu untuk menghilangkan komentar yang tidak relevan.

Pembersihan data dilakukan dengan langkah-langkah berikut:

1. Menghapus komentar yang kosong
2. Menghapus komentar yang hanya berisi emoticon
3. Menghapus komentar yang hanya berisi tag
4. Menghapus komentar yang hanya berisi tautan
5. Menghapus komentar yang hanya berisi kata-kata yang tidak relevan

**Pembentukan Model**

Model LSTM yang digunakan dalam proyek ini terdiri dari 4 lapisan, yaitu:

* Lapisan embedding
* Lapisan LSTM
* Lapisan dense

Lapisan embedding digunakan untuk mengubah input teks menjadi vektor numerik. Lapisan LSTM digunakan untuk mempelajari pola temporal dari sentimen. Lapisan dense digunakan untuk menghasilkan output berupa sentimen.

**Kesimpulan**

Proyek ini berhasil mengembangkan model LSTM yang dapat memprediksi sentimen dari komentar video trailer The Nun 2 dengan akurasi sementara 66%.
