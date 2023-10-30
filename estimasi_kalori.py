import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Membaca model dari file
loaded_model = pickle.load(open('estimasi_kalori.sav', 'rb'))
import streamlit as st

model = pickle.load(open('estimasi_kalori.sav', 'rb'))

st.title('Estimasi Kalori Pada Menu Restoran Dairy Queen')

import streamlit as st

# Daftar pilihan untuk Selectbox
Menu = ["Makanan", "Minuman", "Desert"]

# Daftar pilihan untuk Selectbox
Ukuran = ["Besar", "Sedang", "Kecil"]

# Membuat Selectbox dengan pilihan
selected_option = st.selectbox("Pilih Jenis Menu :", Menu)
selected_option = st.selectbox("Pilih Jenis Ukuran:", Ukuran)
Cholesterol = st.slider ('Masukan Jumlah Cholesterol (mg)', 0,0, 100)
carbohydrates = st.slider('Masukan Total Carbohydrates (g)', 0,0, 72)
Sugars = st.slider('Masukan Jumlah Sugars (g)', 0,0, 72)
Protein = st.slider('Masukan Jumlah Protein (g)', 0, 1000)
Fat_Calories = st.slider ('Masukan Jumlah Fat Calories (kcal)', 15,0, 1510,0)
Sodium = st.slider('Masukan Jumlah Sodium (mg)', 0,0, 100)
Total_Fat = st.slider('Masukan Total Fat (g)', 0,0, 72)

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[Cholesterol, carbohydrates, Sugars, Protein, Fat_Calories, Sodium, Total_Fat]]
        )
    st.write ("Estimasi Jumlah Kalori Menu Makanan Dairy Queen : ", predict)