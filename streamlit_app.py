import streamlit as st
import pandas as pd

# 1. Pastikan ini adalah baris pertama setelah import
st.set_page_config(
    page_title="Dashboard Umum BPS Inhu",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"  # Ini memaksa sidebar terbuka
)

# Sisanya tetap sama...

# Custom CSS (Sudah diperbaiki)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("📊 Dashboard Subbagian Umum")
st.subheader("BPS Kabupaten Indragiri Hulu")
st.info("Selamat datang di pusat kendali administrasi dan manajemen internal.")

# Baris Metrik Utama
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Realisasi Anggaran", "78.5%", "2.1%")
with col2:
    st.metric("Pegawai Aktif", "24 Orang", "0")
with col3:
    st.metric("Kepatuhan ZI", "95%", "Sangat Baik")
with col4:
    st.metric("Aset BMN", "412 Unit", "12 Baru")

st.divider()

# Grafik Sederhana
st.write("### Progres Kegiatan Strategis 2026")
chart_data = pd.DataFrame({
    'Kegiatan': ['Keuangan', 'SDM', 'Risiko', 'ZI/SAKIP', 'BMN'],
    'Progres (%)': [80, 90, 65, 85, 70]
})
st.bar_chart(data=chart_data, x='Kegiatan', y='Progres (%)')

st.success("Gunakan menu di samping kiri untuk melihat detail per bidang.")
