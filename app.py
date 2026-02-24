import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# CSS UNTUK BACKGROUND BIRU LAUT, CORAK BINTANG/LOVE & KOTAK PINK
st.markdown("""
    <style>
    /* 1. Background Biru Laut Pastel dengan Corak */
    .stApp {
        background-color: #E0F7FA !important; /* Biru Laut Pastel */
        background-image: 
            radial-gradient(#FFB6C1 1px, transparent 1px), 
            radial-gradient(#FFD700 1px, transparent 1px);
        background-size: 40px 40px;
        background-position: 0 0, 20px 20px;
    }

    /* 2. Container untuk Header (Logo & Tajuk Sebelah-sebelah) */
    .header-box {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 30px;
        background: rgba(255, 255, 255, 0.6);
        padding: 20px;
        border-radius: 30px;
        margin-bottom: 40px;
        border: 3px solid #FFD1DC;
    }

    /* 3. Tajuk Warna-Warna Gula-Gula */
    .rainbow-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 55px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #FF9AA2, #FFB7B2, #FFDAC1, #E2F0CB, #B5EAD7, #C7CEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(2px 2px 0px #ffffff);
    }

    /* 4. Kotak UI Pink Lembut (Pastikan Tak Jadi Hitam) */
    div[data-baseweb="select"], div[data-baseweb="input"], .stTextArea textarea {
        background-color: #FFD1DC !important; /* Pink Lembut */
        border: 2px solid #FFB6C1 !important;
        border-radius: 15px !important;
    }

    /* Tukar warna tulisan dalam kotak supaya nampak (Bukan Putih/Hitam) */
    div[role="listbox"], div[data-baseweb="select"] *, input {
        color: #7A5C61 !important;
        font-weight: bold !important;
    }

    /* 5. Label Tajuk Kecil */
    .stMarkdown h3 {
        color: #FF8EAD !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    /* 6. Button Jana Prompt */
    .stButton>button {
        background: linear-gradient(135deg, #FFD1DC 0%, #B2F2BB 100%) !important;
        color: #614147 !important;
        border-radius: 50px !important;
        border: 4px solid white !important;
        font-size: 22px !important;
        font-weight: bold !important;
        padding: 15px 30px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION (LOGO + TAJUK) ---
st.markdown('<div class="header-box">', unsafe_allow_html=True)
col_l, col_t = st.columns([1, 3])

with col_l:
    try:
        st.image("logo.png", width=150)
    except:
        st.write("🌸") # Muncul kalau logo.png belum ada

with col_t:
    st.markdown('<h1 class="rainbow-title">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN CONTENT (KOTAK PINK) ---
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("### 🎨 Gaya")
    gaya = st.selectbox("Visual", ["Profesional", "Pastel Soft", "Ceria"], key="v1")
    lajur = st.selectbox("Grid", ["1 Lajur", "2 Lajur", "Grid 2x2"], key="v2")

with c2:
    st.markdown("### 👥 Sasaran")
    audiens = st.selectbox("Audiens", ["Murid", "Guru", "Ibu Papa"], key="s1")
    tema = st.text_input("Tema", placeholder="Taip di sini...", key="s2")

with c3:
    st.markdown("### 📝 Info")
    jenis = st.selectbox("Output", ["Infografik", "Slaid", "Nota"], key="i1")
    nada = st.selectbox("Nada", ["Pendidikan", "Santai"], key="i2")

with c4:
    st.markdown("### 💎 Butiran")
    warna = st.selectbox("Warna", ["Gula-gula", "Sejuk", "Pastel"], key="b1")
    latar = st.selectbox("Latar", ["Putih", "Digital", "Kertas"], key="b2")

# --- BUTTON JANA ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("JANA PROMPT SEKARANG 💗"):
    st.balloons()
    st.markdown("---")
    hasil = f"Buatkan {jenis} {gaya} bertema {tema} untuk {audiens}. Guna warna {warna}."
    st.success("Prompt Berjaya!")
    st.code(hasil, language="text")

st.markdown("<br><center>Disediakan oleh Cikgu Moon - SK Telok Berembang</center>", unsafe_allow_html=True)
