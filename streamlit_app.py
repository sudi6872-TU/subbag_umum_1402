# 3. SIDEBAR (LOGIKA MENU MANUAL)
with st.sidebar:
    st.image("https://www.bps.go.id/id/logo-bps.png", width=100)
    st.title("Navigasi Utama")
    st.write("---")
    
    # Membuat tombol navigasi manual ke halaman di dalam folder pages
    if st.button("👥 Data Personil"):
        st.switch_page("pages/1_Personil.py")
    
    if os.path.exists("pages"):
        st.success("✅ Folder 'pages' terdeteksi")
