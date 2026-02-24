import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# Custom CSS untuk warna Pastel mengikut rujukan gambar
st.markdown("""
    <style>
    /* Latar belakang keseluruhan */
    .stApp {
        background-color: #FDFBFF;
    }
    
    /* Font dan Warna Tajuk */
    h1, h2, h3 {
        color: #FFA7C4 !important; /* Pink Pastel */
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Kotak Input / Sidebar-style containers */
    .stSelectbox, .stMultiSelect, .stTextInput {
        background-color: #F2FFF2; /* Hijau Pastel Sangat Lembut */
        border-radius: 10px;
    }

    /* Button Cantik */
    .stButton>button {
        background-color: #FFD1DC; /* Pink Pastel */
        color: #666;
        border-radius: 20px;
        border: 2px solid #B2F2BB; /* Hijau Pastel */
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #B2F2BB;
        border: 2px solid #FFD1DC;
    }

    /* Kotak Hasil Prompt */
    .result-box {
        background-color: #E8F8F5;
        padding: 20px;
        border-radius: 15px;
        border-left: 10px solid #FFD1DC;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("✨ Chatbot Cikgu Moon")
st.write("Sila pilih kriteria di bawah untuk menjana prompt NotebookLM anda.")

# --- UI LAYOUT (Ikut Gambar Pertama) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎨 Visual & Gaya")
    gaya = st.selectbox("Gaya Kandungan", ["Infografik", "Nota Ringkas", "Kuiz Interaktif", "Cerita Pendek"])
    warna_tema = st.multiselect("Tema Warna", ["Pink Pastel", "Hijau Pastel", "Biru Langit", "Kuning Lembut"], default=["Pink Pastel", "Hijau Pastel"])
    layout_pref = st.radio("Susunan (Grid)", ["1 Lajur", "2 Lajur", "Tiga Segi"])

with col2:
    st.markdown("### 📚 Subjek & Sasaran")
    subjek = st.text_input("Subjek (cth: RBT / BM)", placeholder="Taip subjek di sini...")
    tahap = st.selectbox("Tahap Murid", ["Tahun 1-3", "Tahun 4-6", "Tingkatan 1-3"])
    topik = st.text_area("Topik Spesifik", placeholder="Contoh: Pengenalan kepada Mikropengawal")

with col3:
    st.markdown("### ⚙️ Tetapan Output")
    nada = st.select_slider("Nada Penulisan", options=["Sangat Santai", "Mesra", "Formal"])
    format_output = st.selectbox("Format Fail", ["Teks Markdown", "Jadual", "Senarai Point"])

# --- GENERATE PROMPT ---
st.markdown("---")
if st.button("🚀 JANA PROMPT UNTUK NOTEBOOKLM"):
    prompt_final = f"""
    Hai NotebookLM, saya mahu anda bertindak sebagai pembantu guru. 
    Sila bina kandungan untuk subjek {subjek} bertajuk '{topik}'.
    Sasaran audiens adalah murid {tahap}.
    Gunakan gaya {gaya} dengan nada yang {nada}.
    Untuk susunan visual, cadangkan format {layout_pref} dengan tema warna {', '.join(warna_tema)}.
    Sila hasilkan dalam format {format_output} dalam Bahasa Melayu yang ceria.
    """
    
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("Salin Prompt di Bawah:")
    st.code(prompt_final, language="text")
    st.success("Prompt berjaya dijana! Sila salin dan 'paste' ke dalam NotebookLM Moon.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><hr><center><p style='color: #999;'>Dashboard Chatbot Cikgu Moon | Dibina dengan Streamlit & ❤️</p></center>", unsafe_allow_html=True)
