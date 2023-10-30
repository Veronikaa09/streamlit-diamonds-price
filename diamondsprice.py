import pickle 
import streamlit as st 

model = pickle.load(open('diamond_price.sav', 'rb'))

st.title('Estimasi Harga Berlian')

carat = st.number_input('input berat berlian dalam karat')
depth = st.number_input('input persentase kedalaman berlian')
table = st.number_input('input Lebar titik terlebar berlian')
x = st.number_input('input panjang berlian dalam mm')
y = st.number_input('input Lebar berlian dalam mm')
z = st.number_input('input kedalaman berlian dalam mm')

predict = ''

if st.button('Estimasi Harga Berlian '):
    predict = model.predict(
        [[carat,depth,table,x,y,z]]
    )
    st.write('Estimasi Harga Berlian: ', predict)