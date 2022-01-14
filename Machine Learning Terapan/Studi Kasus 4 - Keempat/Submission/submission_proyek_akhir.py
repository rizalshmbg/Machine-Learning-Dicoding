# -*- coding: utf-8 -*-
"""Submission Proyek Akhir.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eg8rMxcQ75GHkBQ3PKbsaCuYQlyVV2Ml

# Project Overview

Sistem rekomendasi adalah garis pertahanan intuitif terhadap pilihan konsumen yang berlebihan. Mengingat pertumbuhan eksplosif informasi yang tersedia di website belanja online, pengguna sering disambut dengan banyaknya produk yang tawarkan. Dengan demikian, penyesuaian layanannya adalah strategi penting untuk memfasilitasi pengguna untuk membeli produk yang lebih baik.

Secara umum, daftar rekomendasi dihasilkan berdasarkan preferensi pengguna, fitur item, interaksi masa lalu item pengguna dan beberapa informasi lainnya. Sistem ini berperan penting dan tak terpisahkan dalam akses informasi untuk meningkatkan bisnis dan memfasilitasi proses pengambilan keputusan yang melekat di berbagai website belanja online.

Referensi :
* [Deep Learning based Recommender System: A Survey and New Perspectives](https://arxiv.org/pdf/1707.07435.pdf)
* [IJIRST - International Journal for Innovative Research in Science and Technology : Book Recomendation System](https://d1wqtxts1xzle7.cloudfront.net/38839415/IJIRSTV1I11135-with-cover-page-v2.pdf?Expires=1635526606&Signature=OC6kVPB3TytQm7lxnHJoKlHBTx6zf0bgqNhm4jrecRVPCbigc1DYMWwDPoVadTLDWi7l0LqcRj4HReJLsBCyWDlU-ziC8zIQAWdHc8F2PqeXfuXpJcZvyiw0i2ie0R2jyX6lSlkarBEzREi~02wAgD2y10l1cLcDm~rKV1PAx1o~qtMCYe0M7bsfUSAT-n8GD7fxogvEvJhjnN26S1KaYeOTQyyLo5QOfxT6w9Q5tAYMGzdBF-l93PxPdLyUxVztDhUY9E9Tlq1zGc2xBXNWhofh0aRFFAl6xipRe1ntBMB3xZ6atQr8iL4VL8kySLxbYrKqStjmxx4wdbIWDX22Tw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

---

# Business Understanding

Sistem rekomendasi banyak digunakan untuk merekomendasikan produk kepada pengguna. Contohnya situs web penjualan buku online yang saat ini saling bersaing dengan berbagai cara. Sistem rekomendasi adalah salah satu cara yang terbaik untuk meningkatkan keuntungan penjualan dan memperluas jaringan pembeli.

Sistem rekomendasi ini dikembangkan menggunakan algoritma yang dapat menghasilkan berbagai buku yang diminati oleh pembeli, dengan membuat pilihan terbaik berdasarkan preferensi atau data buku yang telah dinilai oleh pengguna sebelumnya.

## Problem Statements

* Bagaimana  sistem rekomendasi menghasilkan sejumlah buku berdasarkan preferensi pengguna ?
* Berdasarkan pada data buku dan rating yang ada, bagaimana  sistem ini dapat merekomendasikan buku-buku yang mungkin disukai oleh pengguna lain?

## Goals

* Untuk merekomendasikan buku kepada pengguna yang dipersonalisasi sesuai dengan minatnya.

* Untuk menghasilkan sejumlah buku yang sesuai dengan preferensi pengguna berdasarkan rating yang telah diberikan sebelumnya.

## Solution Approach

Untuk menyelesaikan masalah ini saya menggunakan dua algoritma sistem rekomendasi sebagai solusi permasalahan yaitu **Content Based Filtering** dan **Collaborative Filtering**.

1. Content Based Filtering \
Teknik Content Based Filtering akan menyaring buku berdasarkan isi buku yang diminati pembeli. Lalu, setiap pengguna dikaitkan dengan pengklasifikasi sebagai profil. Pengklasifikasi mengambil item buku sebagai inputnya dan kemudian menyimpulkan apakah item tersebut disukai oleh pengguna terkait berdasarkan kontennya.    

2. Collaborative Filtering \
Pada tahap ini, sistem akan merekomendasikan sejumlah buku berdasarkan rating yang telah diberikan sebelumnya. Dan akan melihat ke set item yang telah dinilai oleh pengguna lalu menghitung seberapa mirip dengan item target. Dari data rating pengguna, akan mengidentifikasi buku apa saja yang mirip dan belum pernah dibeli oleh pengguna untuk direkomendasikan.

## Mengimpor Library yang Akan Digunakan
"""

# Commented out IPython magic to ensure Python compatibility.
# pengolahan data
import os, sys
import pandas as pd
import numpy as np

# visualisasi data
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
sns.set()

# pemodelan data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

"""---

# Data Understanding

Dataset yang digunakan adalah [Book Recommendation Dataset](https://www.kaggle.com/arashnic/book-recommendation-dataset)

## Menyiapkan Kredensial Akun Kaggle
"""

os.environ['KAGGLE_USERNAME'] = 'rizalsihombing'
os.environ['KAGGLE_KEY'] = '4d09bb88e02a716fc7ea70c27ba33be1'

"""## Mengunduh Dataset"""

!kaggle datasets download -d arashnic/book-recommendation-dataset

"""## Mengekstrak Dataset"""

!unzip book-recommendation-dataset.zip

books = pd.read_csv('/content/Books.csv')
books.info()

"""Dapat dilihat dari Books.csv berjumlah **271360 baris** dan terdapat **7 variabel**, diantaranya adalah :

* ISBN : merupakan kode unik untuk pengidentifikasian buku.
* Book-Title : merupakan judul buku.
* Book-Author : merupakan pengarang atau penulis buku.
* Year-Of-Publication : merupakan tahun penerbitan buku.
* Publisher : merupakan penerbit buku.
* Image-URL-S : merupakan alamat suatu sumber gambar buku yang berukuran kecil, yang mengarah ke website Amazon.
* Image-URL-M : merupakan alamat suatu sumber gambar buku yang berukuran sedang, yang mengarah ke website Amazon.
* Image-URL-L : merupakan alamat suatu sumber gambar buku yang berukuran besar, yang mengarah ke website Amazon.

Namun pada tahap modeling nanti, variabel **Image-URL-S**, **Image-URL-M**, dan **Image-URL-L** tidak butuhkan dan akan dibuang.
"""

ratings = pd.read_csv('/content/Ratings.csv')
ratings.info()

"""Dapat dilihat dari Ratings.csv berjumlah **1149780 baris** dan terdapat **3 variabel**, diantaranya adalah :

* User-ID : merupakan ID atau nomor unik pengguna.
* ISBN : merupakan kode unik untuk pengidentifikasian buku.
* Book-Rating : merupakan nilai peringkat buku yang diberikan oleh pengguna, dinyatakan dalam skala 1-10 (nilai yang lebih tinggi menunjukkan apresiasi yang lebih tinggi).

Setelah melihat dataframe ratings dan books telalu banyak, di sini saya hanya mengambil **10000** baris dari dataset books dan **5000** baris untuk rating dataset
"""

books = books[:10000]
ratings = ratings[:5000]

books.info()

"""---

# Content-Based Filtering

## Data Preparation

Mengubungkan dengan bagian variabel dataset dari **books**, **users**, dan **ratings**
"""

books.columns = ['ISBN', 'BookTitle', 'BookAuthor', 'YearOfPublication',
                 'Publisher', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L']

ratings.columns = ['UserID', 'ISBN', 'BookRating']

"""### Books

Membuang 3 kolom terakhir yang berisi URL gambar karena tidak akan diperlukan. Yaitu :
* Image-URL-S 
* Image-URL-M 
* Image-URL-L
"""

books.drop(['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis=1,inplace=True)

"""Mengecek kembali dataset buku"""

books.dtypes

books.head()

"""Memeriksa nilai yang kosong pada dataset books"""

books.isnull().sum()

"""### Ratings

Memeriksa dataset Ratings.
"""

ratings.BookRating.unique()

ratings.head()

"""Visualisasi Data Ratings."""

plt.style.use('fivethirtyeight')
plt.figure(figsize=(12, 8))
sns.countplot(data=ratings , x='BookRating', palette='rocket_r')

"""Pada visualisasi diagram batang diatas menunjukkan bahwa, rating buku yang lebih tinggi di antara pengguna adalah rating dengan nilai 0. Dan yang tertinggi selanjutnya adalah rating dengan nilai 8.

### Penggabungan Data
"""

book_ISBN = books.ISBN.tolist()
book_Title = books.BookTitle.tolist()
book_Author = books.BookAuthor.tolist()
book_YearOfPublication = books.YearOfPublication.tolist()
book_Publisher = books.Publisher.tolist()

books_new = pd.DataFrame({
    'Book-ISBN': book_ISBN,
    'Book-Title': book_Title,
    'Book-Author': book_Author,
    'Book-YearOfPublication': book_YearOfPublication,
    'Book-Publisher': book_Publisher
})
books_new

"""---

## Modeling and Result

Pada Content Based Filtering, akan menggunakan algoritma TF-IDF Vectorizer untuk membangun sistem rekomendasi berdasarkan penulis buku. TF-IDF yang memiliki fungsi untuk mengukur seberapa pentingnya suatu kata terhadap kata-kata lain dalam dokumen. Secara umum, algoritma akan menghitung skor untuk setiap kata untuk menandakan pentingnya dalam dokumen dan corpus.

* Kelebihan :
 * Model tidak memerlukan data apa pun tentang pengguna lain, membuatnya lebih mudah untuk menskalakan ke sejumlah besar pengguna.
 * Model dapat menangkap minat khusus pengguna, dan dapat merekomendasikan item khusus yang sangat sedikit yang diminati oleh pengguna lain.

* Kekurangan :
 * Karena representasi fitur item direkayasa sampai batas tertentu, teknik ini membutuhkan banyak pengetahuan domain.
 * Model hanya dapat membuat rekomendasi berdasarkan minat pengguna yang ada. Jadi, model memiliki kemampuan terbatas untuk memperluas minat pengguna yang ada.
"""

tf = TfidfVectorizer()
 
tf.fit(books_new['Book-Author']) 
 
tf.get_feature_names()

"""Tahap selanjutnya akan melakukan fit dan transformasi ke dalam matriks tfidf_matrix."""

tfidf_matrix = tf.fit_transform(books_new['Book-Author']) 
 
tfidf_matrix.shape

"""Dapat dilihat bahwa, hasil dari transformasi tfidf_matrix terdapat 10000 ukuran data buku dan 5575 nama penulis buku.

Selanjutnya saya akan menggunakan fungsi todense(), untuk menghasilkan vektor tf-idf dalam bentuk matriks
"""

tfidf_matrix.todense()

"""Dataframe di bawah ini digunakan untuk melihat hasil matriks dari judul buku dengan penulis buku."""

pd.DataFrame(
    tfidf_matrix.todense(), 
    columns = tf.get_feature_names(),
    index = books_new['Book-Title']
).sample(10, axis=1,replace=True).sample(10, axis=0)

"""Selanjutnya, saya akan menghitung derajat kesamaan (similarity degree) antar item yang direkomendasikan agar tidak terlalu jauh dari data pusat dengan teknik cosine similarity dari library sklearn."""

cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

"""Dilanjutkan dengan membuat dataframe variabel cosine_sim_df dengan kolom berupa nama buku."""

cosine_sim_df = pd.DataFrame(cosine_sim, index=books_new['Book-Title'], columns=books_new['Book-Title'])

"""Berikut adalah fungsi untuk mendapatkan hasil rekomendasi sebanyak 5 buku, dengan kesamaan atribut dari penulis buku.

Atribut `argpartition` berguna untuk mengambil sejumlah nilai `k`, karena dalam fungsi menghasilkan sebanyak 5 rekomendasi tertinggi dari tingkat kesamaan yang berasal dari dataframe cosine_sim_df.
"""

def book_recommendations(title, similarity_data=cosine_sim_df, items=books_new[['Book-Title', 'Book-Author']], k=5):
    index = similarity_data.loc[:,title].to_numpy().argpartition(range(-1,-k,-1))
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(title, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)

"""Sebagai contoh, saya akan mencari rekomendasi dari buku yang sudah dibaca. Misalnya buku **Not a Penny More 4** karya **Jeffrey Archer** yang diterbitkan pada tahun 1981."""

readed_book = "Not a Penny More 4"
books_new[books_new['Book-Title'].eq(readed_book)]

"""Dilanjutkan dengan menampilkan 5 rekomendasi dari buku dengan penulisnya adalah **Jeffrey Archer** """

recommendations = book_recommendations(readed_book)
recommendations

"""Dapat dilihat model memberikan 5 buku dengan penulis yang sama, yaitu **Jeffrey Archer**.

---

### Evaluation

Mengevaluasi metrik akurasi, dimana akurasi disini adalah :

Buku yang direkomendasikan sesuai dengan penulis buku / jumlah buku yang direkomendasikan.

Variabel `readed_book_new` merupakan buku yang pernah dibaca sebelumnya. \
Dan variabel `readed_book_author`  adalah buku dengan penulis dari buku yang pernah dibaca sebelumnya
"""

readed_book_new = books[books.BookTitle == readed_book]
readed_book_author = readed_book_new.iloc[0]['BookAuthor']

"""Variabel `book_recommendation_authors` merupakan sebuah list yang terdiri dari para penulis buku-buku yang direkomendasikan oleh sistem ini"""

book_recommendation_authors = recommendations['Book-Author']

"""Kode di bawah ini merupakan proses manual, yang di mana akan mengecek setiap penulis dari buku yang direkomendasikan.Apabila sama, maka variabel `real_author` akan bertambah 1"""

real_author = 0
for i in range(5):
    if book_recommendation_authors[i] == readed_book_author:
        real_author+=1

"""Kode di bawah ini adalah akurasi dari model sistem rekomendasi yang telah dibuat, dimana jumlah buku yang direkomendasikan sesuai dengan penulis buku atau variabel real_author / jumlah buku yang direkomendasikan sebanyak 5."""

acc = real_author / 5*100
print("Akurasi dari model ini adalah {}%".format(acc))

"""Dapat dilihat bahwa akurasi pada model yang telah dibuat menunjukkan **akurasi 100%**.

---

# Collaborative Filtering

## Data Preparation

### Ratings

Mengubah UserID menjadi list tanpa nilai yang sama, lalu melakukan encoding UserID. Dilanjutkan dengan proses encoding angka ke UserId
"""

user_ids = ratings['UserID'].unique().tolist()
print('List UserID: ', user_ids)
 
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('Encoded UserID : ', user_to_user_encoded)
 
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('Encoded angka ke UserID: ', user_encoded_to_user)

"""Mengubah ISBN menjadi list tanpa nilai yang sama, lalu melakukan encoding ISBN. Dilanjutkan dengan proses encoding angka ke ISBN"""

books_ids = ratings['ISBN'].unique().tolist()
print('List ISBN: ', books_ids)
 
book_to_book_encoded = {x: i for i, x in enumerate(books_ids)}
print('Encoded ISBN : ', book_to_book_encoded)

book_encoded_to_book = {i: x for i, x in enumerate(books_ids)}
print('Encoded angka ke ISBN: ', book_encoded_to_book)

"""Memasukkan hasil angka encoding user ke dataframe ratings dengan nama kolom Users. Dan memasukkan hasil angka encoding ISBN ke dataframe ratings dengan nama kolom Books."""

ratings['Users'] = ratings['UserID'].map(user_to_user_encoded)
ratings['Books'] = ratings['ISBN'].map(book_to_book_encoded)

num_users = len(user_encoded_to_user)
print(num_users)
num_book = len(book_encoded_to_book)
print(num_book)
ratings['BookRating'] = ratings['BookRating'].values.astype(np.float32)

min_rating = min(ratings['BookRating'])
max_rating = max(ratings['BookRating'])
 
print('Jumlah dari pengguna: {}, Jumlah dari buku: {}, Rating minimal: {}, Rating maksimal: {}'.format(
    num_users, num_book, min_rating, max_rating
))

"""Mengacak datanya agar distribusinya menjadi random."""

ratings = ratings.sample(frac=1, random_state=42)
ratings

"""Membagi data latih dan data validasi dengan komposisi 80:20."""

x = ratings[['Users', 'Books']].values
 
y = ratings['BookRating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values
 
train_indices = int(0.80 * ratings.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)
 
print(x, y)

"""---

## Modeling and Result

Diawal, akan melakukan proses embedding terhadap data user dan buku. Selanjutnya, lakukan operasi perkalian dot product antara embedding pengguna dan buku. Selain itu, kita juga dapat menambahkan bias untuk setiap pengguna dan buku. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid. Dilanjutkan dengan membuat class RecommenderNet dengan keras Model. Class RecommenderNet ini terinspirasi dari tutorial dalam situs Keras dengan beberapa adaptasi sesuai dengan kasusnya.

* Kelebihan :
 * Hanya berfokus pada konten dan tidak memberikan kemampuan beradaptasi apa pun pada preferensi dan aspek pengguna.
 *  Sistem ini hanya membutuhkan matriks umpan balik untuk melatih model faktorisasi matriks. Secara khusus, sistem tidak memerlukan fitur kontekstual.

* Kekurangan :
 * Sistem rekomendasi ini tidak dapat membuat penyematan dan mengkueri model untuk item yang merupakan barang baru.
 * Sulit untuk menyertakan fitur sampingan untuk kueri/item.
"""

from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf

class RecommenderNet(tf.keras.Model):
 
  def __init__(self, num_users, num_book, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_book = num_book
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1)
    self.book_embedding = layers.Embedding( 
        num_book,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.book_bias = layers.Embedding(num_book, 1) 
 
  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0])
    user_bias = self.user_bias(inputs[:, 0])
    book_vector = self.book_embedding(inputs[:, 1])
    book_bias = self.book_bias(inputs[:, 1]) 
 
    dot_user_resto = tf.tensordot(user_vector, book_vector, 2) 
 
    x = dot_user_resto + user_bias + book_bias
    
    return tf.nn.sigmoid(x)

"""Selanjutnya, melakukan proses compile terhadap model menggunakan Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer, dan root mean squared error (RMSE) sebagai metrics evaluation."""

model = RecommenderNet(num_users, num_book, 50)

model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Proses training."""

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 5,
    epochs = 50,
    validation_data = (x_val, y_val)
)

"""### Visualisasi Metrik

Visualisasi proses hasil latihan dari data, evaluasi metrik yang digunakan adalah RMSE.
"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""Mendapatkan Hasil Rekomendasi Buku"""

books_df = books
ratings_df = ratings

ratings_df

"""Selanjutnya akan mengambil sampel Users secara acak dari dataset rating. Dari User ini kita perlu mengetahui buku apa saja yang pernah dibaca sebelumnya, dan buku apa saja yang belum pernah dibaca. Sehingga model akan dapat merekomendasikan buku yang belum pernah dibaca."""

user_id = ratings_df.UserID.sample(1).iloc[0]
book_readed = ratings_df[ratings_df.UserID == user_id]
 
book_not_readed = books_df[~books_df['ISBN'].isin(book_readed.ISBN.values)]['ISBN'] 
book_not_readed = list(
    set(book_not_readed)
    .intersection(set(book_to_book_encoded.keys()))
)
 
book_not_readed = [[book_to_book_encoded.get(x)] for x in book_not_readed]
user_encoder = user_to_user_encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(book_not_readed), book_not_readed)
)

"""Proses yang akan memperoleh rekomendasi 10 buku dari pengguna."""

Ratings = model.predict(user_book_array).flatten()
 
top_ratings_indices = Ratings.argsort()[-10:][::-1]
recommended_book_ids = [
    book_encoded_to_book.get(book_not_readed[x][0]) for x in top_ratings_indices
]
 
print('Menampilkan rekomendasi untuk User: {}'.format(user_id))
print('===' * 9)
print('Buku dengan rating tertinggi dari User')
print('----' * 8)
 
top_books_recommended = (
    book_readed.sort_values(
        by = 'BookRating',
        ascending=False
    )
    .head(5)
    .ISBN.values
)
 
books_row = books_df[books_df['ISBN'].isin(top_books_recommended)]
for row in books_row.itertuples():
    print(row.BookTitle, ':', row.BookAuthor)
 
print('----' * 8)
print('Top 10 - Rekomendasi Buku untuk User')
print('----' * 8)
 
recommended_books = books_df[books_df['ISBN'].isin(recommended_book_ids)]
for row in recommended_books.itertuples():
    print(row.BookTitle, ':', row.BookAuthor)

"""Referensi :
* [Dicoding - Model Development dengan Content Based Filtering](https://www.dicoding.com/academies/319/tutorials/19657)
* [Dicoding - Model Development dengan Collaborative Filtering](https://www.dicoding.com/academies/319/tutorials/19662)
* https://www.kaggle.com/arashnic/recom-i-data-understanding-and-simple-recomm
* https://www.kaggle.com/hetulmehta/book-recommendation-system#notebook-container
* https://towardsdatascience.com/
* https://towardsdatascience.com/my-journey-to-building-book-recommendation-system-5ec959c41847
"""