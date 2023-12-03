import streamlit as st

st.set_page_config(
    page_title="Organizational Experience|Nabila",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Pengalaman Organisasi")
st.write("Hanya Satu Organisasi Yang Saya Ikuti; ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("Team Tour Indonesia")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("organisasi.jpg", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Menjabat Sebagai Anggota Team Tour Indonesia*")
   