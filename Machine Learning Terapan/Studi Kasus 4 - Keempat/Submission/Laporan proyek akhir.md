# Laporan Sistem Rekomendasi Buku - Rizal Sihombing

## Project Overview
Sistem rekomendasi adalah garis pertahanan intuitif terhadap pilihan konsumen yang berlebihan. Mengingat pertumbuhan eksplosif informasi yang tersedia di website belanja online, pengguna sering disambut dengan banyaknya produk yang tawarkan. Dengan demikian, penyesuaian layanannya adalah strategi penting untuk memfasilitasi pengguna untuk membeli produk yang lebih baik.

Secara umum, daftar rekomendasi dihasilkan berdasarkan preferensi pengguna, fitur item, interaksi masa lalu item pengguna dan beberapa informasi lainnya. Sistem ini berperan penting dan tak terpisahkan dalam akses informasi untuk meningkatkan bisnis dan memfasilitasi proses pengambilan keputusan yang melekat di berbagai website belanja online.

Referensi :
* [Deep Learning based Recommender System: A Survey and New Perspectives](https://arxiv.org/pdf/1707.07435.pdf)
* [IJIRST - International Journal for Innovative Research in Science and Technology : Book Recomendation System](https://d1wqtxts1xzle7.cloudfront.net/38839415/IJIRSTV1I11135-with-cover-page-v2.pdf?Expires=1635526606&Signature=OC6kVPB3TytQm7lxnHJoKlHBTx6zf0bgqNhm4jrecRVPCbigc1DYMWwDPoVadTLDWi7l0LqcRj4HReJLsBCyWDlU-ziC8zIQAWdHc8F2PqeXfuXpJcZvyiw0i2ie0R2jyX6lSlkarBEzREi~02wAgD2y10l1cLcDm~rKV1PAx1o~qtMCYe0M7bsfUSAT-n8GD7fxogvEvJhjnN26S1KaYeOTQyyLo5QOfxT6w9Q5tAYMGzdBF-l93PxPdLyUxVztDhUY9E9Tlq1zGc2xBXNWhofh0aRFFAl6xipRe1ntBMB3xZ6atQr8iL4VL8kySLxbYrKqStjmxx4wdbIWDX22Tw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

## Business Understanding
Sistem rekomendasi banyak digunakan untuk merekomendasikan produk kepada pengguna. Contohnya situs web penjualan buku online yang saat ini saling bersaing dengan berbagai cara. Sistem rekomendasi adalah salah satu cara yang terbaik untuk meningkatkan keuntungan penjualan dan memperluas jaringan pembeli.

Sistem rekomendasi ini dikembangkan menggunakan algoritma yang dapat menghasilkan berbagai buku yang diminati oleh pembeli, dengan membuat pilihan terbaik berdasarkan preferensi atau data buku yang telah dinilai oleh pengguna sebelumnya.

### Problem Statements
* Bagaimana  sistem rekomendasi menghasilkan sejumlah buku berdasarkan preferensi pengguna ?
* Berdasarkan pada data buku dan rating yang ada, bagaimana  sistem ini dapat merekomendasikan buku-buku yang mungkin disukai oleh pengguna lain?

### Goals
* Untuk merekomendasikan buku kepada pengguna yang dipersonalisasi sesuai dengan minatnya.
* Untuk menghasilkan sejumlah buku yang sesuai dengan preferensi pengguna berdasarkan rating yang telah diberikan sebelumnya.

### Solution approach
Untuk menyelesaikan masalah ini saya menggunakan dua algoritma sistem rekomendasi sebagai solusi permasalahan yaitu **Content Based Filtering** dan **Collaborative Filtering**.

1. Content Based Filtering
Teknik Content Based Filtering akan menyaring buku berdasarkan isi buku yang diminati pembeli. Lalu, setiap pengguna dikaitkan dengan pengklasifikasi sebagai profil. Pengklasifikasi mengambil item buku sebagai inputnya dan kemudian menyimpulkan apakah item tersebut disukai oleh pengguna terkait berdasarkan kontennya. \

2. Collaborative Filtering
Pada tahap ini, sistem akan merekomendasikan sejumlah buku berdasarkan rating yang telah diberikan sebelumnya. Dan akan melihat ke set item yang telah dinilai oleh pengguna lalu menghitung seberapa mirip dengan item target. Dari data rating pengguna, akan mengidentifikasi buku apa saja yang mirip dan belum pernah dibeli oleh pengguna untuk direkomendasikan.

## Data Understanding
Dataset yang digunakan adalah [Book Recommendation Dataset](https://www.kaggle.com/arashnic/book-recommendation-dataset). Yang terdiri dari **Books.csv**, **Ratings.csv**.
Dari **Books.csv** berjumlah **271360 baris** dan terdapat **7 variabel**, diantaranya adalah :

* ISBN : merupakan kode unik untuk pengidentifikasian buku.
* Book-Title : merupakan judul buku.
* Book-Author : merupakan pengarang atau penulis buku.
* Year-Of-Publication : merupakan tahun penerbitan buku.
* Publisher : merupakan penerbit buku.
* Image-URL-S : merupakan alamat suatu sumber gambar buku yang berukuran kecil, yang mengarah ke website Amazon.
* Image-URL-M : merupakan alamat suatu sumber gambar buku yang berukuran sedang, yang mengarah ke website Amazon.
* Image-URL-L : merupakan alamat suatu sumber gambar buku yang berukuran besar, yang mengarah ke website Amazon.
Namun pada tahap modeling nanti, variabel **Image-URL-S**, **Image-URL-M**, dan **Image-URL-L** tidak butuhkan dan akan dibuang.

Dari **Ratings.csv** berjumlah **1149780 baris** dan terdapat **3 variabel**, diantaranya adalah :

* User-ID : merupakan ID atau nomor unik pengguna.
* ISBN : merupakan kode unik untuk pengidentifikasian buku.
* Book-Rating : merupakan nilai peringkat buku yang diberikan oleh pengguna, dinyatakan dalam skala 1-10 (nilai yang lebih tinggi menunjukkan apresiasi yang lebih tinggi).

Visualisasi data Ratings menggunakan diagram batang :

![image](https://user-images.githubusercontent.com/66808677/140025036-7698fcd9-b4fe-4e28-a776-53f5ab0679d6.png)

Pada visualisasi diagram batang diatas menunjukkan bahwa, rating buku yang lebih tinggi di antara pengguna adalah rating dengan nilai 0. Dan yang tertinggi selanjutnya adalah rating dengan nilai 8.

## Data Preparation
Pada tahap ini saya melakukan proses :
* Mengurangi karena jumlah baris datasetnya terlalu banyak yaitu pada Books.csv berjumlah 271360 baris, dan Ratings.csv berjumlah 1149780 baris. Maka saya mengambilnya **10000 baris pada Books.csv** dan **5000 baris pada Ratings.csv**.
* Membuang kolom, karena ada 3 kolom pada dataset Books.csv yang tidak akan digunakan yaitu **Image-URL-S**, **Image-URL-M**, **Image-URL-L**.

Pada tahap **Content Based Filtering** saya melakukan :
* Mengubah dataset buku menjadi sebuah list, karena nantinya list ini akan digunakan untuk diubah ke dictionary baru yg akan menjadi landasan pada pembuatan model sistem rekomendasi.
* Memasukkan list ke dalam dictionary baru. Setelah sebelumnya membuat list diperlukan untuk membuat dictionary yang digunakan untuk memnentukan pasangan key-value pada **Book-ISBN**, **Book-Title**, **Book-Author**, **Book-YearOfPublication**, dan **Book-Publisher**.

Pada tahap **Collaborative Filtering** saya melakukan :
* Mengubah UserID menjadi list tanpa nilai yang sama, lalu melakukan encoding UserID. Dilanjutkan dengan proses encoding angka ke UserId.
* Mengubah ISBN menjadi list tanpa nilai yang sama, lalu melakukan encoding ISBN. Dilanjutkan dengan proses encoding angka ke ISBN.
* Mengacak data, agar distribusinya menjadi random.
* Membagi data latih dan data validasi dengan komposisi 80:20.

## Modeling
1. **Content Based Filtering**.
Pemodelan menggunakan algoritma TF-IDF Vectorizer untuk membangun sistem rekomendasi berdasarkan penulis buku. TF-IDF yang memiliki fungsi untuk mengukur seberapa pentingnya suatu kata terhadap kata-kata lain dalam dokumen. Secara umum, algoritma akan menghitung skor untuk setiap kata untuk menandakan pentingnya dalam dokumen dan corpus. Tahap selanjutnya melakukan fit dan transformasi ke dalam matriks tfidf_matrix. Dilanjutkan dengan menggunakan fungsi todense(), untuk menghasilkan vektor tf-idf dalam bentuk matriks. Lalu selanjutnya melakukan perhitungan derajat kesamaan (similarity degree) antar item yang direkomendasikan agar tidak terlalu jauh dari data pusat dengan teknik cosine similarity dari library sklearn. Dilanjutkan dengan membuat dataframe variabel cosine_sim_df dengan kolom berupa nama buku. Dan terakhir adalah membuat fungsi untuk mendapatkan hasil rekomendasi sebanyak 5 buku, dengan kesamaan atribut dari penulis buku.
* Kelebihan :
  * Model tidak memerlukan data apa pun tentang pengguna lain, membuatnya lebih mudah untuk menskalakan ke sejumlah besar pengguna.
  * Model dapat menangkap minat khusus pengguna, dan dapat merekomendasikan item khusus yang sangat sedikit yang diminati oleh pengguna lain.

* Kekurangan :
  * Karena representasi fitur item direkayasa sampai batas tertentu, teknik ini membutuhkan banyak pengetahuan domain.
  * Model hanya dapat membuat rekomendasi berdasarkan minat pengguna yang ada. Jadi, model memiliki kemampuan terbatas untuk memperluas minat pengguna yang ada.

Setelah itu pengguna akan mencari rekomendasi dari buku yang sudah dibaca. Misalnya buku **Not a Penny More 4** karya **Jeffrey Archer** yang diterbitkan pada tahun 1981.
```{python}
Book-Title	Book-Author
0	Kane &amp; Abel	Jeffrey Archer
1	A TWIST IN THE TALE	Jeffrey Archer
2	Sons of Fortune (Ay Adult - Archer)	Jeffrey Archer
3	The Eleventh Commandment	Jeffrey Archer
4	To Cut a Long Story Short	Jeffrey Archer
```
Dapat dilihat model memberikan 5 buku dengan penulis yang sama, yaitu **Jeffrey Archer**.

2. **Collaborative Filtering**
Diawal, akan melakukan proses embedding terhadap data user dan buku. Selanjutnya, lakukan operasi perkalian dot product antara embedding pengguna dan buku. Selain itu, kita juga dapat menambahkan bias untuk setiap pengguna dan buku. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid. Dilanjutkan dengan membuat class RecommenderNet dengan keras Model. Class RecommenderNet ini terinspirasi dari tutorial dalam situs Keras dengan beberapa adaptasi sesuai dengan kasusnya. Dilanjutkan dengan melakukan proses compile terhadap model. Selanjutnya, melakukan proses compile terhadap model menggunakan Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer, dan root mean squared error (RMSE) sebagai metrics evaluation, dilanjutkan ke proses training. Selanjutnya akan mengambil sampel Users secara acak dari dataset rating. Dari User ini kita perlu mengetahui buku apa saja yang pernah dibaca sebelumnya, dan buku apa saja yang belum pernah dibaca. Sehingga model akan dapat merekomendasikan buku yang belum pernah dibaca.
* Kelebihan :
  * Hanya berfokus pada konten dan tidak memberikan kemampuan beradaptasi apa pun pada preferensi dan aspek pengguna.
  *  Sistem ini hanya membutuhkan matriks umpan balik untuk melatih model faktorisasi matriks. Secara khusus, sistem tidak memerlukan fitur kontekstual.

* Kekurangan :
  * Sistem rekomendasi ini tidak dapat membuat penyematan dan mengkueri model untuk item yang merupakan barang baru.
  * Sulit untuk menyertakan fitur sampingan untuk kueri/item.

Berikut adalah hasil modelnya :
```{python}
Menampilkan rekomendasi untuk User: 278131
===========================
Buku dengan rating tertinggi dari User
--------------------------------
Five Quarters of the Orange : Joanne Harris
--------------------------------
Top 10 - Rekomendasi Buku untuk User
--------------------------------
To Kill a Mockingbird : Harper Lee
Life of Pi : Yann Martel
Lord of the Flies : William Gerald Golding
The King of Torts : JOHN GRISHAM
Politically Correct Bedtime Stories: Modern Tales for Our Life and Times : James Finn Garner
The Door into Summer : Robert A. Heinlein
Die zweite Haut. : Dean Koontz
I Am Legend : Richard Matheson
The Watsons Go to Birmingham - 1963 (Yearling Newbery) : CHRISTOPHER PAUL CURTIS
Last Man Standing : David Baldacci
```
Dapat dilihat model memberikan hasil buku dengan rating tertinggi dari penilaian user yaitu **The Etruscan Chimera (Archaeological Mystery)**, dan model juga memberikan rekomendasi 10 buku lainnya. 

## Evaluation
1. **Content-Based Filtering**
Mengevaluasi metrik akurasi, dimana akurasi disini adalah. Buku yang direkomendasikan sesuai dengan penulis buku / jumlah buku yang direkomendasikan.
 * Pertama adalah dengan membuat variabel readed_book_new merupakan buku yang pernah dibaca sebelumnya. Dan variabel readed_book_author adalah buku dengan penulis dari buku yang pernah dibaca sebelumnya.
 * Kedua, membuat sebuah looping yang merupakan proses manual di mana setiap penulis dari buku yang direkomendasikan akan dicek. Apabila sama maka variabel real_author akan bertambah 1.
 * Lalu hasilnya dapat dilihat dengan kode di bawah ini. Yang merupakan hasil akurasi dari model sistem rekomendasi yang telah dibuat, dimana jumlah buku yang direkomendasikan sesuai dengan penulis buku atau variabel real_author / jumlah buku yang direkomendasikan sebanyak 5 buku.
```{python}
acc = real_author / 5*100
print("Akurasi dari model ini adalah {}%".format(acc))
```
Keluaran :
```python
Akurasi dari model ini adalah 100.0%
```

2. **Collaborative Filtering**
Evaluasi metrik yang digunakan adalah RMSE (root-mean-square error).

![image](https://user-images.githubusercontent.com/66808677/140503396-2febd461-2449-4cd3-9d1f-521f767ec6ae.png)


Adalah ukuran yang sering digunakan untuk perbandingan antara nilai yang diprediksi oleh model dan nilai yang diamati. Keakuratan metode estimasi kesalahan (error) pengukuran ditandai dengan adanya nilai RMSE yang kecil. Metode estimasi yang mempunyai Root Mean Square Error (RMSE) lebih kecil dikatakan lebih akurat daripada metode estimasi yang mempunyai Root Mean Square Error (RMSE) lebih besar. Berikut adalah rumus nya :
* At = Nilai data aktual
* Ft = Nilai hasil prediksi
* N = Banyaknya data
* ∑ = Summation (Jumlahkan keseluruhan  nilai)

RMSE di-definisikan pada bagian metriks dalam model, kemudian di-visualisasikan lewat grafik :
```python
plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
```
Visualisasi :

![image](https://user-images.githubusercontent.com/66808677/140039561-18e564d2-9288-4677-81af-080ad3628237.png)
