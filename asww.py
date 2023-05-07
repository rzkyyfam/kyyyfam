import streamlit as st

st.title(':violet[Octagram]')
st.header('Webbs :blue[Konfersi PPM]')

option = st.selectbox('Konfersi PPM Ke?',('Normalitas','Molaritas','%(b/b)','%(b/v)'))


if option == 'Normalitas':
    ppm = st.number_input('Masukkan Nilai PPM')
    be = st.number_input('Masukkan Nilai Berat Ekivalen(BE)',value = 1.00)
    
    st.button('Hitung Nilai Normalitas')
    nilai_normalitas = round(((ppm/be)/1000),4)
    st.success(f'Nilai Normalitas Adalah {nilai_normalitas}')
elif option == 'Molaritas':
    ppm = st.number_input('Masukkan Nilai PPM')
    bm = st.number_input('Masukkan Nilai Berat Molekul(BM)') 
    
    st.button('Hitung Nilai Molaritas')
    nilai_molaritas = (ppm/bm)/1000
    st.success(f'Nilai Molaritas Adalah {nilai_molaritas}')
    
elif option == '%(b/b)':
    ppm = st.number_input('Masukkan Nilai PPM mg/Kg')
    st.button('Hitung Nilai %(b/b)')
    nilai_bb = (ppm/10000)
    st.success(f'Nilai %(b/b) adalah {nilai_bb}%')
    
else :
    ppm = st.number_input('Masukkan Nilai PPM mg/L') 
    st.button('Hitung Nilai %(b/v)')
    nilai_bv = (ppm/10000)
    st.success(f'Nilai %(b/v) adalah {nilai_bv}%')
    
    
    

    
    
    

