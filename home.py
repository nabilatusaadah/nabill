import streamlit as st
st.set_page_config(
    page_title="Portfolio | nabila",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")
st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("isun.jpg", width= 390)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : NABILATUS SAADAH")
   st.caption("NIM : 0402201088")
   st.write(
            """
            - Tempat Tanggal Lahir : Pekalongan 27 Desember 2002 
            - Alamat               : Pegaden Tengah Wonopringgo Pekalongan
            - Hobi                 : scroll sosmed
            - Cita-cita            : Jadi Orang Manfaat
            - Hal yang disukai     : nyemil
            - Status               : Hamba Allah
            """
        )
   col1, = st.columns(1)
with col1:
     
    st.image("ig.png", width= 50)
    st.link_button("Instagram", "https://instagram.com/kang_rokhman?igshid=YTQwZjQ0NmI0OA%3D%3D")

st.header("*Call Me If You Want*")
