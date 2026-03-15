import streamlit as st
import pandas as pd
import os

# 1. KONFIGURASI HALAMAN (WAJIB BARIS PERTAMA)
st.set_page_config(
    page_title="Dashboard Umum BPS Inhu",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SIDEBAR (NAVIGASI MANUAL)
# 2. SIDEBAR (LOGIKA NAVIGASI YANG BENAR)
with st.sidebar:
    st.image("https://www.bps.go.id/id/logo-bps.png", width=100)
    st.title("Navigasi Utama")
    st.write("---")
    
    # Bungkus st.switch_page di dalam IF tombol
    # Ini memastikan koding hanya jalan saat diklik
    if st.button("👥 Buka Data Personil"):
        try:
            st.switch_page("pages/1_Personil.py")
        except:
            st.error("Gagal pindah halaman. Cek apakah file 'pages/1_Personil.py' ada di GitHub.")

# 3. KONTEN UTAMA
st.title("📊 Dashboard Subbagian Umum")
st.subheader("BPS Kabupaten Indragiri Hulu")

st.info("Selamat datang di pusat kendali administrasi dan manajemen internal.")

# Baris Metrik
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

# Grafik Progres
st.write("### 📈 Progres Kegiatan Strategis 2026")
chart_data = pd.DataFrame({
    'Kegiatan': ['Personil', 'Adm. Umum', 'SDM', 'Risiko'],
    'Progres (%)': [85, 70, 90, 65]
})
st.bar_chart(data=chart_data, x='Kegiatan', y='Progres (%)')

st.success("Pilih menu di samping kiri untuk melihat detail.")
