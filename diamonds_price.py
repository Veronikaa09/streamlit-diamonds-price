import pickle
import streamlit as st 

model = pickle.load(open('diamonds_price.sav', 'rb'))

st.title('harga berlian')

carat = st.number_input('input berat berlian dalam karat')
depth = st.number_input('input persentase kedalaman berlian')
table = st.number_input('input Lebar titik terlebar berlian')
x = st.number_input('input panjang berlian dalam mm')
y = st.number_input('input Lebar berlian dalam mm')
z = st.number_input('input kedalaman berlian dalam mm')

predict = ''

if st.button('Harga berlian'):
predict = model.predict(
[[carat,depth,table,x,y,z]]
)
st.write('harga berlian dalam milimeter : ',predict)
st.write('harga berlian dalam IDR (Juta) : ',predict*19000)
