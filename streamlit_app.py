import streamlit as st
import pandas as pd
import os

# 1. KONFIGURASI HALAMAN (Wajib di baris pertama)
st.set_page_config(
    page_title="Dashboard Umum BPS Inhu",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded" # Memaksa sidebar terbuka
)

# 2. CSS UNTUK TAMPILAN
st.markdown("""
    <style>
    /* Mengatur warna latar belakang */
    .stApp {
        background-color: #0e1117;
    }
    /* Mengatur gaya teks */
    h1, h2, h3 {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (LOGIKA CEK FOLDER)
with st.sidebar:
    st.image("https://www.bps.go.id/id/logo-bps.png", width=100) # Logo BPS jika ada internet
    st.title("Navigasi Utama")
    st.write("---")
    
    # Cek apakah folder 'pages' terbaca oleh sistem
    if os.path.exists("pages"):
        st.success("✅ Folder 'pages' terdeteksi")
    else:
        st.error("❌ Folder 'pages' tidak ditemukan")
        st.info("Pastikan nama folder di GitHub adalah 'pages' (huruf kecil semua)")

# 4. KONTEN HALAMAN UTAMA
st.title("📊 Dashboard Subbagian Umum")
st.subheader("BPS Kabupaten Indragiri Hulu")

# Row 1: Metrik Utama
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

# Row 2: Grafik Progres
st.write("### 📈 Progres Kegiatan Strategis 2026")
chart_data = pd.DataFrame({
    'Kegiatan': ['Personil', 'Adm. Umum', 'SDM', 'Risiko'],
    'Progres (%)': [85, 70, 90, 65]
})
st.bar_chart(data=chart_data, x='Kegiatan', y='Progres (%)', color="#29b5e8")

# Pesan Bantuan
st.info("💡 Tip: Jika menu di samping kiri belum muncul, klik tombol 'Manage app' di pojok kanan bawah lalu pilih 'Reboot app'.")
