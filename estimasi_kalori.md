# Laporan Proyek Machine Learning
### Nama  : Debrina Azzahra
### Nim   : 211351155
### Kelas : TIF Malam B

## Domain Proyek
Seperti dalam masalah kesehatan dan kebugaran dalam hal ini
banyak aplikasi dan perangkat yang fokus pada estimasi kalori untuk membantu
seseorang dalam mengelola pola makan dan aktivitas fisik mereka guna mencapai tujuan kesehatan dan kebugaran. Domain ini mungkin mencakup perhitungan kalori yang terbakar selama latihan, menghitung asupan kalori harian, dan memantau progres kebugaran. 

**Rubrik/Kriteria Tambahan (Opsional)**:<br>

Aplikasi ini memungkinkan individu untuk memantau asupan kalori harian mereka dan memastikan bahwa mereka tidak mengkonsumsi terlalu banyak atau terlalu sedikit kalori saat hendak makan di Daily Queen. 

Format Referensi: [Dairy Queen Menu Nutrition Dataset](https://www.kaggle.com/datasets/mattop/dairy-queen-menu-nutrition-data) 

# BUSINESS UNDERSTANDING
Pada tahap ini Bagaimana membangun atau mendapatkan data, dan bagaimana untuk mencocokan tujuan pemodelan untuk tujuan bisnis restorant sehingga model terbaik dapat dibangun.

### Problem Statements
Dairy Queen di American memiliki berbagai macam menu dengan jumlah kandungan gizi yang tentunya berbeda-beda. Maka dari itu, Dairy Queen 
mencantumkan kompoisi di setiap menu makanan yang dibantu oleh pakar kesehatan dan ahli diet, apakah mengkonsumsi makanan dengan melihat dan menghitung asupan kalori dengan tidak berlebihan nar dan sesuai yang dibutuhkan oleh tubuh dapat mempengaruhi kadar kolesterol, protein, karbohidrat, total lemak dan gula tanpa khawatir pelanggan terkena penyakit kronis.

### Goals
Dataset yang di ambil dari kaggle bertujuan untuk menganalisis dan mengetahui estimasi jumlah kalori dari menu makanan Dairy Queen, agar 
pelanggan dapat lebih memahami kandungan gizi dan sadar akan apa yang mereka makan agar dapat mengelola kesehatan tubuh dengan lebih baik.

### Rubrik/Kriteria Tambahan (Opsional) :
**Solution statements**<br>
- Dengan estimasi kalori ini, pelanggan dapat melacak asupan kalori sehingga mereka dapat mengelola pola makan mereka dengan lebih baik. Solusi ini dapat membantu menjelaskan manfaat dan fitur-fitur utama dari estimasi kalori di restoran Dairy Queen, serta dapat membantu pelanggan dalam mengelola kesehatan dan pola makan mereka dengan lebih baik.
= Solusi kedua menggunakan model yang dihasilkan dari dataset menggunakan metode Linear Regression.

## Data Understanding

Tahap ini, membuat ringkasaan (summary) dan mengidentifikasi potensi masalah m data. Tahap ini juga harus dilakukan secara cermat dan tidak terburu-buru, seperti pada visualisasi data, yang terkadang insight-nya sulit didapat dika dihubungkan dengan summary data nya. Jika ada masalah pada tahap ini yang belum terjawab, maka akan menggangu pada p modeling. Dataset yang saya gunakan berasal jadi Kaggle yang didapat dari menu-menu pada restoran dairy queen yang berada diAmerika.
set ini mengandung 229 baris dan lebih 9 kolom.<br> 

Dataset: [Dairy Queen Menu Nutrition Dataset](https://www.kaggle.com/datasets/mattop/dairy-queen-menu-nutrition-data) 

### Variabel-variabel pada Heart Failure Prediction Dataset adalah sebagai berikut:

- Menu          (Menentukan ukuran menu)            = objek (Ukuran : Besar, sedang, kecil)
- Calories      (Menentukan jumlah kalori)          = int [Numbers, Min: 0, Max: 1000 kcal]
- Fat_Calories  (Menentukan jumlah lemak kalori )   = int [Numbers, Min: 0, Max: 1000 kcal]
- Total_fat     (Menentukan jumlah lemak total)     = float [Numbers, Min: 0, Max: 1000 kcal]
- Cholesterol   (Menentukan jumalah kolestrol)      = int [Numbers, Min: 0, Max: 1000 kcal]
- Sodium        (Menentukan jumlah sodium)          = int [Numbers, Min: 0, Max: 1000 kcal]
- Carbohydrate  (Menentukan jumlah karbohidrat)     = int [Numbers, Min: 0, Max: 1000 kcal]
- Sugars        (Menentukan jumlah gula)            = int [Numbers, Min: 0, Max: 1000 kcal]
- Protein       (Menentukan jumlah protein)         = float [Numbers, Min: 0, Max: 1000 kcal]

## Data Preparation
**Data Collection**<br>
Untuk data collection ini, saya mendapatkan dataset yang nantinya digunakan dari website kaggle dengan nama dataset Dairy Queen Menu Nutrition Dataset

**Data Discovery And Profiling**<br>
Teknik EDA.

## Library yang akan digunakan
**Data Discovery And Profiling**<br>
Teknik EDA.<br>

Mengimport semua library yang dibutuhkan,

    import pandas as pd
    import numpy as np
    import matplotlib.pypot as plt
    import seaborn as sns

 ## Deskripsi Dataset
Karena kita memakai googgle collab bukan csv maka kita Import file 

    from google.colab import files

Upload token kaggle agar nanti bisa mendownload sebuah dataset dari kaggle melalui google colab

    file.upload()

Setelah mengupload filenya, selanjutnya membuat folder untuk menyimpan file kaggle.json yang sudah diupload tadi

    !mkdir -p ~/.kaggle
    !cp kaggle.json ~/.kaggle/
    !chmod 600 ~/.kaggle/kaggle.json
    !ls ~/.kaggle

Lalu download datasetsnya

    !kaggle datasets download -d mattop/dairy-queen-menu-nutrition-data --force

Extract file yang tadi telah didownload

    !mkdir dairy-queen-menu-nutrition-data
    !unzip dairy-queen-menu-nutrition-data.zip -d dairy-queen-menu-nutrition-data
    !ls dairy-queen-menu-nutrition-data

Menampilkan 5 data paling atas dari datasetsnya

    df = pd.read_csv("/content/drive/MyDrive/estimasi_kalori/dairy_queen.csv")
    df.head(5)

## DATA PREPARATION
Menampilkan informasi ringkas tentang tabel data dalam pandas

    df.info()

Fungsi yang digunakan untuk membuat heat.map dalam Seaborn. Haat.map ini akan menampilkan data yang hilang dalam DataFrame dengan warna tertentu, yang memungkinkan untuk secara visual melihat di mana data hilang.

    sns.heatmap(df.isnull())

Metode ini memberikan gambaran cepat tentang statistik dasar dari setiap kolom numerik dalam DataFrame.

    df.describe()

Hasilnya akan menjadi kumpulan scatter plot yang membentuk matriks. Diagonal dari matriks tersebut akan berisi histogram dari masing-masing variabel. Diagonal atas dan bawah akan berisi scatter plot yang menunjukkan hubungan antara pasangan variabel.

    sns.set_theme(style="white")
    sns.despine()

    sns.pairplot(df);

Kode yang Anda tunjukkan menggunakan pustaka Seaborn dan Matplotlib untuk membuat matriks korelasi dan menampilkan heatmap dari korelasi antara variabel-variabel numerik dalam DataFrame df.

    plt.figure(figsize=(15,8))
    sns.heatmap(df.corr(), annot=True)

Digunakan untuk menemukan dan mengekstrak baris-baris dalam DataFrame df yang memiliki nilai yang identik di semua kolomnya. Ini berarti baris-baris yang sama persis dalam setiap atribut atau variabel.

    df[df.duplicated()]

Digunakan untuk menghapus baris-baris yang merupakan duplikat dari DataFrame df

    df.drop_duplicates(inplace=True)


## Jumlah Kalori
mengelompokkan data dalam DataFrame df berdasarkan kolom 'Protein', menghitung jumlah munculnya setiap nilai unik dalam kolom 'Protein', mengurutkannya berdasarkan kolom 'Total_Fat' secara ascending (dari nilai terendah ke tertinggi), dan kemudian mereset indeksnya. Setelah itu, Anda mengganti nama kolom 'Total_Fat' menjadi 'Calories'. 

    brands = df.groupby('Protein').count()[['Total_Fat']].sort_values(by='Total_Fat', ascending=True).reset_index()
    brands = brands.rename(columns={'Total_Fat':'Calories'})

Membuat diagram batang (barplot) menggunakan Seaborn. Pada diagram ini, sumbu x (horizontal) akan berisi nilai dari kolom 'Protein' dari DataFrame brands, sedangkan sumbu y (vertikal) akan berisi nilai dari kolom 'Calories' dari DataFrame brands. Data ini akan diwakili dalam bentuk batang-barang, di mana nilai 'Protein' akan berada di sumbu x dan jumlah 'Calories' akan diwakili oleh tinggi batang. Seluruh batang pada diagram ini akan berwarna hijau, sesuai dengan parameter color='green' yang Anda berikan. 

Ini berlaku untuk semua tabel, tinggal diganti saja dan dibandingan dengan tabel calories


    fig = plt.figure(figsize = (20,7))
    sns.barplot(x = brands['Menu'], y = brands['Calories'], color = 'green')
    plt.xticks(rotation = 60)

## Modeling

Import library 

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

Memasukkan kolom-kolom fitur yang ada di datasets dan juga kolom targetnya

    fitur = ['Cholesterol', 'Sugars', 'Fat_Calories', 'Total_Fat', 'Carbohydrates', 'Sodium', 'Protein']
    x = df[fitur]
    y = df['Calories']
    x.shape, y.shape

Untuk membagi dataset menjadi data pelatihan (train) dan data pengujian (test).

    x_train, X_test, y_train, y_test = train_test_split(x, y, random_state = 70)
    y_test.shape

Membuat model Linear Regressionnya

    model = LinearRegression()

Import modul LinearRegression dari scikit-learn

    from sklearn.linear_model import LinearRegression

Inisialisasi model regresi linear

    lr = LinearRegression()

Melatih model dengan data pelatihan

    lr.fit(x_train, y_train)

Melakukan prediksi

    predik = lr.predict(X_test)

Mengukur akurasi model regresi linear dengan membandingkan hasil prediksi model pada data pengujian 

    y = lr.score(X_test, y_test)
    print('Akurasi Model Regresi Linier : ', y)

Hasilnya 0.9991840271557658. Untuk memprediksi jumlah kalori berdasarkan nilai-nilai yang diberikan. Hasil prediksi akan disimpan dalam variabel prediksi 

    #Cholesterols(mg) = 125 , Carbohydrate(g) = 37 , Sugars(g) = 7 , Protein(g) = 34, Total_Fat(g) = 49, Fat_Calories(kg) = 21, Sodium(kg) = 56,
    inputan = np.array([[125, 37, 7, 34, 49, 21, 56]])
    prediksi = lr.predict(inputan)
    print('Estimasi Jumlah Energi dalam setiap size menu  : ', prediksi)

Jika modelnya sudah selesai, kemudian export sebagai sav untuk bisa digunakan pada web streamlit.

    import pickle
    filename = 'estimasi_kalori.sav'
    pickle.dump(lr,open(filename,'wb'))

## Evaluation

Untuk melakukan prediksi dengan model regresi linear (lr) pada data fitur pengujian (X_test). Hasil prediksi akan disimpan dalam variabel predictions

    predictions = lr.predict(X_test)

Metrik ini memberikan informasi tentang model regresi dalam memprediksi data. Semakin kecil nilai MAE, MSE, dan RMSE, semakin baik kualitas prediksi model. 

    from sklearn import metrics
    print('MAE:', metrics.mean_absolute_error(y_test, predictions))
    print('MSE:', metrics.mean_squared_error(y_test, predictions))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

Hasilnya <br>
MAE: 5.694105493866003 <br>
MSE: 66.56722285450142 <br>
RMSE: 8.158873871711796 <br>

Sebagai contoh, MAE sekitar 5.694 mengindikasikan bahwa rata-rata selisih absolut antara prediksi model dan nilai sebenarnya adalah sekitar 
5.694 unit. MSE dan RMSE memberikan perspektif tambahan, dengan RMSE sekitar 8.159 yang merupakan akar kuadrat dari MSE, dan ini menggambarkan sejauh mana prediksi bervariasi dari nilai sebenarnya dalam satuan yang sama dengan data asli.

Dengan memeriksa nilai variance yang dijelaskan, dapat memahami sejauh mana model yang mampu menjelaskan variasi dalam data pengujian. Semakin tinggi nilai explained variance, semakin baik model Anda dalam menjelaskan variasi dalam data target. 

    print('Variance:', metrics.explained_variance_score(y_test, predictions))

Hasil sudah di jalankan adalah 0.999186076445628

## Deployment

[Estimasi Kalori Daily Queen](https://estimasi-kalori-pada-menu-di-restorant-daily-queen-dhyssagnxvj.streamlit.app/)



