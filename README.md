# Metode_Numerik_2026
Tugas Akhir Semester 2026

Untuk soal Numerik 11.1 dan 11.3 di mana menggunakan 2 cara yaitu:
- Kodenya melakukan dua perjalanan:Maju (Forward Elimination): Program menyapu dari baris pertama sampai terakhir untuk menghilangkan angka-angka di "bahu jalan bawah" (sub-diagonal). Saat ini dilakukan, angka di diagonal utama dan nilai di sebelah kanan (vektor hasil) otomatis ikut menyesuaikan.
- Mundur (Backward Substitution): Setelah angka bawahnya bersih (nol semua), program memutar balik dari baris terbawah ke atas. Karena baris paling bawah sekarang sisa satu variabel saja, kita bisa langsung dapat jawabannya. Jawaban ini lalu disubstitusi (dimasukkan) ke baris atasnya berturut-turut sampai semua nilai variabel x ketemu.

Kemudian untuk soal 11.2 konsep daasarnya:
Mencari invers matriks itu intinya sama dengan mencari jawaban dari sistem persamaan, tapi ruas kanannya diganti dengan matriks identitas (matriks yang isinya angka 1 di diagonal, sisanya 0).
- Pertama, fungsi la.lu(A) dari pustaka scipy akan membelah matriks asal menjadi dua bentuk segitiga: Segitiga Bawah (Lower/L) dan Segitiga Atas (Upper/U).
- Lalu, program melakukan perulangan (looping). Di setiap putaran, program mengambil satu kolom dari matriks identitas (ini yang disebut unit vector di soal).
- Program kemudian melakukan substitusi maju pada matriks L, disusul substitusi mundur pada matriks U. Hasil akhirnya ditempelkan sebagai satu kolom di matriks invers kita yang baru. Proses ini diulang sampai semua kolom terisi.

Untuk soal 11.4 sampai 11.7: Dekomposisi Cholesky
cara kerjanya seperti:
- Untuk memecah matriks, kita tinggal memanggil mantra np.linalg.cholesky(A) dari NumPy. Ini langsung memberikan kita matriks L.Soal 11.5 & 11.6: Sama seperti logika dekomposisi LU tadi, setelah dapat matriks L, program menyelesaikan persamaannya dengan cara jalan maju, lalu jalan mundur menggunakan transpose dari matriks L tersebut.
- Soal 11.4: Ini murni soal pembuktian. Kodenya hanya mengalikan matriks L hasil Cholesky dengan transposenya. Lalu ada fungsi np.allclose() yang mengecek, "Apakah hasil kali ini angkanya sama persis dengan matriks asli kita?" Kalau sama, berarti metodenya terbukti valid.
- Soal 11.7: Matriks di soal ini isinya nol semua kecuali di diagonal tengah. Program Cholesky cukup mengakarkan angka-angka di tengah itu (akar 9 jadi 3, akar 25 jadi 5, dan akar 4 jadi 2) sesuai aturan dasarnya.

Lalu unutk soal 11.8:
Program memulai dengan tebakan awal.
- Di setiap putaran, program menghitung nilai variabel pertama. Hebatnya Gauss-Seidel, begitu nilai variabel pertama ini didapat yang lebih akurat, nilai ini langsung dipakai untuk menebak variabel kedua di baris yang sama. Begitu seterusnya.
- Di soal ini ada instruksi khusus: overrelaxation dengan nilai lambda = 1.2. Di dalam kode, tebakan baru tadi dicampur dengan tebakan lama menggunakan faktor pengali 1.2. Ibaratnya, program menyuruh perhitungannya "lari sedikit lebih jauh" dari arah tebakannya supaya lebih cepat sampai di garis finish (konvergen).
- Di akhir setiap putaran, program menghitung selisih persentase antara tebakan baru dan lama. Kalau selisih semua variabel sudah di bawah 5%, looping otomatis berhenti dan memunculkan jawabannya.

Untuk 11.9 - 11.10:
Keduanya adalah metode tebak-tebakan (iteratif), tapi beda gaya kerjanya, yaitu:
- Jacobi: Ibarat ngumpulin tugas kelompok, Jacobi nunggu semua tebakan variabel baru selesai dihitung, baru nilainya di-update bareng-bareng untuk putaran berikutnya.
- Gauss-Seidel: Dia lebih agresif. Begitu nilai x₁ yang baru dihitung, nilai fresh ini langsung dipakai untuk ngitung x₂ di detik itu juga.
Dalam hal ini ada pengecekan kondisi if metode == 'gauss_seidel'. Kalau ya, program akan menjumlahkan menggunakan campuran data x baru yang sudah ada dan x lama. Kalau pilihannya jacobi, program secara murni cuma pakai array x_old (data lama) buat hitung putaran saat itu.

Soal 11.11 - 11.13:
Di dalam kode Python, sebelum kita serahkan ke fungsi iterasi, kita coba menukar urutan baris matriks aslinya terlebih dahulu secara manual. Misalnya, persamaan yang koefisien x₁-nya paling besar  taruh di baris pertama, yang x₂-nya paling besar di baris kedua, dst. Setelah rapi, baru bisa iterasi sampai konvergen.

11.14: Kalau kemiringan (slope) persamaannya sama persis, bentuknya di grafik adalah dua garis yang saling sejajar.
11.15: Set soal ketiga tidak bisa disusun ulang agar dominan secara diagonal. Kodenya cuma untuk membuktikan kalau dipaksakan, angka error-nya akan terus membengkak (divergen).

11.16: Pada soal ini, cara kerjanya adalah menggunakan fungsi bawaan NumPy untuk menyelesaikan sistem persamaan linear matriks 4x4, mencari inversnya, dan menghitung condition number. Khusus untuk mencari condition number, kode disetel menggunakan parameter p=np.inf untuk menghitung "row-sum norm". Artinya, program menjumlahkan nilai mutlak di tiap baris dan mencari baris dengan total paling besar, yang berguna untuk mengetahui seberapa rentan matriks tersebut terhadap kesalahan pembulatan komputer.

11.17: Pada soal ini, cara kerjanya berfokus pada pencarian titik temu dua persamaan non-linear menggunakan fungsi fsolve dari SciPy. Karena persamaannya melengkung (mengandung nilai kuadrat), titik potongnya bisa lebih dari satu. Oleh karena itu, kode memberikan sebuah list berisi beberapa "tebakan awal" koordinat. Fungsi fsolve kemudian akan bergerak dari masing-masing titik tebakan tersebut untuk mencari akar penyelesaian terdekat secara numerik.

11.18: Pada soal ini, cara kerjanya adalah menerjemahkan masalah ketersediaan material pabrik menjadi matriks matematika murni. Kebutuhan tembaga, seng, dan kaca diletakkan sebagai baris matriks, sedangkan produknya sebagai kolom. Setelah dibentuk menjadi matriks koefisien dan vektor ketersediaan barang, program memanggil fungsi solusi linear standar untuk langsung menghitung berapa tepatnya jumlah transistor, resistor, dan cip yang harus diproduksi agar bahan bakunya habis tanpa sisa.

11.19: Pada soal ini, cara kerjanya adalah mengukur tingkat ketidakstabilan dari Matriks Hilbert berukuran 10x10. Program menghitung spectral condition number (menggunakan parameter p=2). Karena matriks ini sangat sensitif (ill-conditioned), kode juga menghitung nilai logaritma basis 10 dari hasil condition number tersebut. Perhitungan logaritma ini digunakan sebagai estimasi untuk mengetahui seberapa banyak digit presisi di belakang koma yang akan "hilang" atau eror saat komputer menyelesaikan matriks tersebut.

11.20: Pada soal ini, cara kerjanya serupa dengan 11.19, namun diuji pada Matriks Vandermonde 6x6. Kodenya pertama-tama membentuk matriks secara otomatis dengan memangkatkan input nilai x yang diberikan. Setelah menghitung condition number dan perkiraan presisi yang hilang, program membuktikan ketidakstabilan ini dengan menyelesaikan sistem persamaannya, lalu membandingkan hasil hitungan Python dengan jawaban aslinya untuk melihat persentase eror secara nyata.11.21: Pada soal ini, cara kerjanya murni untuk memanipulasi bentuk array di Python. Kode menggunakan fungsi np.hstack (penggabungan horizontal) untuk menempelkan Matriks A dengan sebuah matriks identitas yang seukuran. Ini adalah simulasi cara membuat matriks augmented, yang merupakan tahapan awal jika kita ingin melakukan proses eliminasi matriks secara manual.

11.21: Pada soal ini, cara kerjanya murni untuk memanipulasi bentuk array di Python. Kode menggunakan fungsi np.hstack (penggabungan horizontal) untuk menempelkan Matriks A dengan sebuah matriks identitas yang seukuran. Ini adalah simulasi cara membuat matriks augmented, yang merupakan tahapan awal jika kita ingin melakukan proses eliminasi matriks secara manual.

11.22: Pada soal ini, cara kerjanya didasarkan pada penyusunan ulang persamaan aljabar. Persamaan di soal sengaja dibuat berantakan (variabel ada di ruas kiri dan kanan). Di dalam kode, diasumsikan variabelnya sudah dipindahkan ke ruas kiri dan konstantanya di kanan. Begitu rapi dan masuk ke dalam matriks, program tinggal mengeksekusi tiga perintah dasar NumPy secara berurutan: mencari nilai variabel, menukar baris jadi kolom (transpose), dan membalik matriksnya (invers).

11.23: Pada soal ini, cara kerjanya adalah menghitung dan membandingkan beban komputasi antara Eliminasi Gauss biasa dan Algoritma Thomas. Kode membuat array ukuran matriks dari 2 hingga 20. Untuk tiap ukuran, program memasukkannya ke rumus beban kerja Gauss dan rumus beban kerja Thomas. Lewat angka-angka yang dihasilkan, program membuktikan bahwa untuk matriks tridiagonal, menggunakan Algoritma Thomas jauh lebih ringan bagi CPU komputer daripada harus repot-repot menggunakan Eliminasi Gauss.

11.24, 11.25, 11.26: Pada ketiga soal ini, cara kerjanya adalah membungkus ulang logika rumit dari Algoritma Thomas, Cholesky, dan Gauss-Seidel menjadi fungsi-fungsi Python yang siap pakai (user-friendly). Kodenya dibuat agar nantinya pengguna cukup memanggil fungsinya dan memasukkan matriks mereka sendiri. Untuk memastikan blok fungsinya bekerja, di dalam kode disertakan data uji coba (dummy data) yang akan otomatis dihitung saat program dijalankan.

11.24, 11.25, 11.26: Pada ketiga soal ini, cara kerjanya adalah membungkus ulang logika rumit dari Algoritma Thomas, Cholesky, dan Gauss-Seidel menjadi fungsi-fungsi Python yang siap pakai (user-friendly). Kodenya dibuat agar nantinya pengguna cukup memanggil fungsinya dan memasukkan matriks mereka sendiri. Untuk memastikan blok fungsinya bekerja, di dalam kode disertakan data uji coba (dummy data) yang akan otomatis dihitung saat program dijalankan.

11.27: Pada soal ini, cara kerjanya adalah mendiskritisasi (mencacah) persamaan diferensial menjadi bentuk aljabar linear menggunakan metode Beda Hingga (Finite Difference). Kode menghitung bobot koefisien aliran dan difusi. Karena setiap titik di kanal hanya terpengaruh oleh titik persis di kiri dan kanannya, susunan koefisien ini otomatis membentuk matriks tridiagonal. Angka 80 dan 20 dimasukkan ke vektor ruas kanan sebagai kondisi batas, lalu program menyelesaikannya untuk mendapatkan nilai konsentrasi di titik-titik tengahnya.

11.28: Pada soal ini, cara kerjanya adalah menjalankan sebuah fungsi efisien khusus untuk sistem pentadiagonal (matriks dengan satu diagonal utama dan masing-masing dua diagonal pendamping di atas dan bawahnya). Kodenya bekerja layaknya Algoritma Thomas, namun dengan area sapuan yang lebih lebar (5 lajur). Agar array tidak error karena membaca indeks kosong saat baris pertama dan terakhir dieliminasi, kode menambahkan elemen nol sementara (padding), melakukan eliminasi maju, dan diakhiri dengan substitusi mundur.

