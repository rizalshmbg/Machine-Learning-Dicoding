# Laporan Proyek Machine Learning - Rizal Sihombing

## Domain Proyek
Tenggelamnya Titanic adalah sebuah bencana kapal pesiar yang terkenal pada pelayaran perdananya. Kapal RMS Titanic yang digadang-gadang "tidak dapat tenggelam", akhirnya tenggelam di bagian utara samudera Atlantik pada tanggal 15 April 1912. Dan menewaskan 1502 dari 2224 penumpang dan awak kapal. Meskipun ada beberapa elemen keberuntungan yang terlibat untuk selamat, tampaknya beberapa kelompok orang lebih mungkin untuk selamat daripada yang lain. Analisis data tentang "orang seperti apa yang lebih mungkin untuk selamat?"  menggunakan data penumpang (yaitu nama, usia, jenis kelamin, kelas tiket, dll). Pendekatan yang dilakukan adalah dengan memanfaatkan kumpulan data umum yang tersedia dari situs web yang dikenal seperti [Kaggle](https://www.kaggle.com/c/titanic/data).

Referensi :
* http://csis.pace.edu/~ctappert/srd2014/d3.pdf
* https://www.researchgate.net/profile/Neytullah-Acun/publication/324909545_A_Comparative_Study_on_Machine_Learning_Techniques_Using_Titanic_Dataset/links/607533bc299bf1f56d51db20/A-Comparative-Study-on-Machine-Learning-Techniques-Using-Titanic-Dataset.pdf


## Business Understanding
Kumpulan data ini merekam berbagai fitur penumpang di Titanic, termasuk siapa yang selamat dan siapa yang tidak. Disadari bahwa beberapa fitur yang hilang dan tidak berkorelasi mengurangi kinerja prediksi. Untuk analisis data rinci, efek dari fitur telah diselidiki. Jadi beberapa fitur baru ditambahkan ke dataset dan beberapa fitur yang ada dihapus dari kumpulan data.

### Problem Statements (Pernyataan Masalah)
Bagaimana cara mengetahui penumpang yang akan selamat dari data yang ada?

### Goals (Tujuan)
* Mengetahui fitur yang paling berpengaruh terhadap keselamatan penumpang.
* Untuk mendapatkan hasil yang dapat mendekati prediksi dari data mentah, dengan menggunakan pembelajaran mesin dan metode rekayasa fitur.

### Solution Statements (Pernyataan Solusi)
Mengetahui fitur apa saja yang berpengaruh terhadap keselamatan penumpang Titanic dan dapat memprediksi penumpang yang selamat dan tidak selamat. Maka, metodologi pada proyek ini adalah membangun model regresi dengan fitur _survived_ sebagai target. Dan, memprediksi penumpang yang dapat selamat dan tidak selamat dengan klasifikasi. Menggunakan :
1. KNN (K-Nearest Neighbor) \
Mengklasifikasikan objek baru berdasarkan atribut dan sampel-sampel dari pelatihan data.
2. Decision Tree \
Prediksi menggunakan struktur pohon atau struktur berhirarki. Lalu mengeliminasi perhitungan atau data-data yang tidak diperlukan. Sebab, sampel yang ada biasanya hanya diuji berdasarkan kriteria atau kelas tertentu saja.
3. Random Forest \
Merupakan salah satu metode dalam Decision Tree, dan kombinasi dari masing-masing tree yang diperlukan kemudian dikombinasikan ke dalam satu model. Random Forest bergantung pada sebuah nilai vector random dengan distribusi yang sama pada semua pohon yang masing-masing decision tree memiliki kedalaman yang maksimal.
4. Super Vector Machine (Classifier) \
Algoritma yang bertujuan untuk memaksimalkan margin antara pola pelatihan dan batas kepututsan, dengan sebuah bidang yang mampu memisahkan dua buah kelas.

## Data Understanding (Pemahaman Data)
Data yang digunakan pada proyek kali ini adalah Titanic dataset, yang dapat diunduh dari [Kaggle](https://www.kaggle.com/c/titanic/data). \
train.csv berjumlah 891 baris, sedangkan test.csv 418 baris.

### Variabel atau fitur pada Titanic dataset adalah sebagai berikut :
Memeriksa tipe data pada setiap variable dengan menggunakna fungsi info(). Untuk implementasi code sebagai berikut :
* data latih :
```python
train.info()
```
Hasil keluaran :
```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
```
* data tes :
```python
test.info()
```
Hasil keluaran :
```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 418 entries, 0 to 417
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  418 non-null    int64  
 1   Pclass       418 non-null    int64  
 2   Name         418 non-null    object 
 3   Sex          418 non-null    object 
 4   Age          332 non-null    float64
 5   SibSp        418 non-null    int64  
 6   Parch        418 non-null    int64  
 7   Ticket       418 non-null    object 
 8   Fare         417 non-null    float64
 9   Cabin        91 non-null     object 
 10  Embarked     418 non-null    object 
dtypes: float64(2), int64(4), object(5)
memory usage: 36.0+ KB
```
* PassengerId : Id penumpang
* Pclass : kelas tiket. 1 = 1st, 2 = 2nd, 3 = 3rd
* Survived : penumpang yang selamat,0 = Tidak, 1 = Ya
* Name : nama penumpang
* Sex : jenis kelamin penumpang. 0 = laki-laki, 1 = perempuan
* Age : umur penumpang
* SibSp : Sibling & Spouse yang artinya jumlah saudara kandung atau pasangan yang dibawa oleh penumpang
* Parch : jumlah keluarga atau anak yang dibawa oleh penumpang
* Ticket : id atau nomor tiket penumpang
* Fare : tarif tiket. 0 = kurang dari 17 Poundsterling (UK), 1 = lebih dari 17 Poundsterling (UK), 2 = lebih dari 30 Poundsterling (UK), 3 = lebih dari 100 Poundsterling (UK)
* Cabin : kategori kabin. A = 0.0, B = 0.4, C = 0.8, D = 1.2, E = 1.6, F = 2.0, G = 2.4, T = 2.8
* Embarked : dari pelabuhan mana penumpang naik. C = Cherbourg, Q = Queenstown, S = Southampton
* Title : pengelompokkan penumpang contohnya apakah penumpang tersebut sudah menikah atau belum. 0 = Mr, 1 = Miss, 2 = Mrs, 3 = Lainnya
* FamilySize : jumlah dari SibSp ditambah dengan Parch. 1= 0, 2= 0.4, 3= 0.8, 4= 1.2, 5= 1.6, 6= 2, 7= 2.4, 8= 2.8, 9= 3.2, 10= 3.6, 11= 4


## Data Preparation
Pada tahap ini saya menerapkan proses :
1. Data Cleaning, karena ada beberapa kolom yang berisi nilai NaN
2. Data Integration, saya menggabungkan kolom SibSp dengan Parch menjadi NumOfFamily karena dua kolom ini memiliki pemahaman yang sama
3. Data Transformation, saya menggunakan teknik ini pada kolom Name menjadi Title untuk mempermudah pembacaan fitur dan memperoleh data yang lebih berkualitas
4. Data Encoding, saya menggunakan teknik data ordinal encoding yaitu setiap nilai kategorik dengan rentang nilai tertentu akan diberi nilai integer


## Modeling
Pertama, yaitu melakukan validasi silang menggunakan **Cross Validation (K-Fold)**, yaitu parameter untuk membagi sampel data dalam rangkaian data latih dan data uji. Dengan memisahkan kumpulan data menjadi (k) lipatan berurutan yang jumlah lipatannya 10. Kemudian akan digunakan satu kali sebagai validasi, sedangkan (k-1) lipatan yang tersisa akan membentuk dataset latih.

Parameter `shuffle=True` akan mengacak data sebelum dipecah menjadi beberapa kelompok yang mempengaruhi urutan indeks, dan mengontrol keacakan setiap lipatan.

Parameter `random_state=0` digunakan untuk menginisialisasi generator nomor acak internal, yang akan memutuskan pemisahan data menjadi data latih dan menguji indeks. Karena disini bernilai 0, maka nilai yang diinisialisasi secara acak akan dikembalikan lagi nilai yang berbeda.

Dilanjutkan dengan menggunakan `cross_val_score`, yaitu metode yang dapat digunakan untuk mengevaluasi kinerja model atau algoritma, dimana data dipisahkan menjadi dua subset yaitu data proses latih dan data validasi.

Parameternya :
1. `estimator`, yaitu algoritma yang digunakan untuk pemrosesan.
2. `X`, yaitu variabel input atau fitur yang akan digunakan.
3. `y`, yaitu variabel tujuan (target) untuk mencoba memprediksi nilai.
4. `cv`, yaitu metode strategi pemisahan validasi silang.
5. `n_jobs`, yaitu jumlah pekerjaan untuk dijalankan secara paralel.
6. `scoring`, fungsi yang dipanggil pencetak skor dengan  estimator, X, y, hanya mengembalikan satu nilai.

Pada tahap ini, saya mengembangkan model machine learning dengan empat algoritma. Kemudian mengevaluasi performa masing-masing algoritma dan menentukan algoritma apa yang memberikan hasil prediksi terbaik.
* K-Nearest Neighbor \
Yaitu klasifikasi berbasis tetangga dengan jenis pembelajaran berbasis instansi atau pembelajaran non-generalisasi. K-NN tidak mencoba membangun model internal umum, tetapi hanya menyimpan nilai instansi dari data pelatihan. Dengan nilai tetangga (nilai terdekat) yang akan digunakan sebanyak 13. \
Menghasilkan skor rata-rata **82.6**

* Decision Tree \
Yaitu membuat model yang memprediksi nilai variabel target dengan mempelajari aturan keputusan sederhana yang disimpulkan dari fitur data dilihat sebagai pendekatan konstan sepotong demi sepotong. \
Menghasilkan skor rata-rata **79.46**

* Random Forest \
Yaitu meta estimator yang cocok dengan sejumlah pengklasifikasi pohon keputusan pada berbagai sub-sampel dari dataset dan menggunakan rata-rata untuk meningkatkan akurasi prediksi dan kontrol over-fitting. Dengan jumlah nilai pohon sebanyak 13. \
Menghasilkan skor rata-rata **81.71**

* Super Vector Machine (Classifier) \
Yaitu pemodelan klasifikasi yang memiliki konsep lebih matang dan lebih jelas secara matematis dibandingkan dengan teknik klasifikasi lainnya. Karena algoritma ini efektif dalam ruang dimensi tinggi walaupun jumlah dimensinya lebih besar dari jumlah sampel dan menggunakan subset titik pelatihan dalam fungsi keputusan. \
Menghasilkan skor rata-rata **83.5**

Setelah melakukan pemodelan data dengan keempat algoritma diatas, didapatkan bahwa pemodelan menggunakan algoritma **Super Vector Machine (Classifier)** mendapatkan hasil rata-rata akurasi tertinggi yaitu = **83.5**.

Model Super Vector Machine (Classifier) ini bisa dijadikan model solusi yang akan digunakan.


## Evaluation
Untuk evaluasi model, disini saya menggunakan matriks **precision**.

Sebelum ke metrik evaluasi, terlebih dahulu kita harus mengerti tentang **Confusion Matrix**.
Confusion matriks menggambarkan kinerja model klasifikasi pada dataset uji yang nilai sebenarnya diketahui untuk mewakili prediksi. Di dalam confusion matrix, terdapat 4 kesimpulan, diantaranya :
* True Positive (TP): True positive mewakili nilai prediksi positif yang benar dari kasus positif aktual. 
* False Positive (FP): False positive mewakili nilai prediksi positif yang salah.
* True Negative (TN): True negative mewakili nilai prediksi yang benar dari negatif dari kasus negatif yang sebenarnya.
* False Negative (FN): False negative mewakili nilai prediksi negatif yang salah.

**Precision**
Precision adalah kemampuan model untuk memprediksi nilai positif dengan benar dari semua prediksi positif yang dibuatnya, dan ukuran yang berguna dari keberhasilan prediksi ketika kelas sangat tidak seimbang.

Formula Precision :
* TP – True Positives
* FP – False Positives
* Precision = TP/(TP + FP)

Untuk menerapkan kode dan hasil dari evaluasi model yang sudah dibuat menjadi seperti ini :
```python
print(classification_report(target, target_pred))
```
Keluaran :
```python
              precision    recall  f1-score   support

           0       0.85      0.89      0.87       549
           1       0.82      0.75      0.78       342

    accuracy                           0.84       891
   macro avg       0.83      0.82      0.83       891
weighted avg       0.84      0.84      0.84       891

```
Precision terhadap **label 0 atau penumpang yang tidak selamat adalah 85%** dan **label 1 atau penumpang yang akan selamat adalah 82%**. Dengan pengertian bahwa **model dapat memprediksi dengan benar terhadap label 0 (penumpang yang tidak selamat) sebanyak 85%** dan **terhadap label 1 (penumpang yang akan selamat) sebanyak 82%**.
