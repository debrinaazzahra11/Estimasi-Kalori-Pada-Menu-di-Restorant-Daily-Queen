import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Membaca model dari file
loaded_model = pickle.load(open('estimasi_kalori.sav', 'rb'))
import streamlit as st

model = pickle.load(open('estimasi_kalori.sav', 'rb'))

st.title('Estimasi Kalori Pada Restoran Dairy Queen')

import streamlit as st

# Daftar pilihan untuk Selectbox
Menu = ["Makanan", "Minuman", "Desert"]

# Daftar pilihan untuk Selectbox
Ukuran = ["Besar", "Sedang", "Kecil"]

# Membuat Selectbox dengan pilihan
selected_option = st.selectbox("Pilih Jenis Menu :", Menu)
selected_option = st.selectbox("Pilih Jenis Ukuran:", Ukuran)
Cholesterol = st.number_input ('Masukan Jumlah Cholesterol (mg)')
carbohydrates = st.number_input ('Masukan Total Carbohydrates (g)')
Sugars = st.number_input ('Masukan Jumlah Sugars (g)')
Protein = st.number_input ('Masukan Jumlah Protein (g)')
Fat_Calories = st.number_input  ('Masukan Jumlah Fat Calories (kcal)')
Sodium = st.number_input ('Masukan Jumlah Sodium (mg)')
Total_Fat = st.number_input ('Masukan Total Fat (g)')

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[Cholesterol, carbohydrates, Sugars, Protein, Fat_Calories, Sodium, Total_Fat]]
        )
    st.write ("Estimasi Jumlah Kalori Menu Makanan Dairy Queen : ", predict)
    
# Mengambil input dari pengguna untuk informasi nutrisi
    calories = float(input("Masukkan jumlah kalori: "))
    total_fat = float(input("Masukkan jumlah lemak (gram): "))

# Menghitung "fat calories" (kalori dari lemak)
    fat_calories = total_fat * 9
# Mengambil input dari pengguna untuk informasi nutrisi
calories = float(input("Masukkan jumlah kalori: "))
total_fat = float(input("Masukkan jumlah lemak (gram): "))

# Menghitung "fat calories" (kalori dari lemak)
fat_calories = total_fat * 9

# Menentukan apakah "fat calories" tinggi atau tidak
if fat_calories > 300:
    status_fat_calories = "tinggi"
else:
    status_fat_calories = "tidak tinggi"

# Menampilkan hasil
print(f"Makanan ini memiliki 'fat calories' {status_fat_calories}.")