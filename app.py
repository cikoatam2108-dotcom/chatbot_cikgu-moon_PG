import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# CSS FIX: TEMA PASTEL, KOTAK PINK, NO BLACK!
st.markdown("""
    <style>
    /* 1. Background Biru Laut dengan Corak Pastel */
    .stApp {
        background-color: #E0F7FA !important;
        background-image: radial-gradient(#FFB6C1 2px, transparent 2px), radial-gradient(#FFD700 2px, transparent 2px);
        background-size: 50px 50px;
        background-position: 0 0, 25px 25px;
    }

    /* 2. Header: Logo Besar & Tajuk Rainbow Sebelah-sebelah */
    .header-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        gap: 30px;
    }

    .rainbow-text {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 50px;
        font-weight: bold;
        background: linear-gradient(to right, #FF9AA2, #FFB7B2, #FFDAC1, #E2F0CB, #B5EAD7, #C7CEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(2px 2px 0px white);
    }

    /* 3. Kotak Input Pink Lembut (BUANG HITAM) */
    div[data-baseweb="select"], div[data-baseweb="input"], .stTextArea textarea {
        background-color: #FFE4E1 !important; /* Pink Lembut */
        border: 2px solid #FFC0CB !important;
        border-radius: 15px !important;
        color: #7A5C61 !important;
    }

    /* Tulisan dalam kotak dan label */
    label p, .stMarkdown p, span {
        color: #7A5C61 !important;
        font-weight: bold !important;
    }

    /* 4. Button Jana (Pastel & Cantik) */
    .stButton>button {
        background: linear-gradient(to right, #FFD1DC, #B2F2BB) !important;
        color: #7A5C61 !important;
        border: 3px solid white !important;
        border-radius: 25px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 300px;
        height: 60px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    /* Buang garisan putih panjang yang tak guna */
    hr {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col_img, col_title = st.columns([1.5, 5])
with col_img:
    try:
        st.image("logo.png", width=250) # Saiz gambar dibesarkan
    except:
        st.write("🌸")
with col_title:
    st.markdown('<br><h1 class="rainbow-text">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)

# --- BORANG UI (3 LAJUR KEMAS) ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### ✨ Keutamaan Gaya")
    gaya = st.selectbox("Gaya Visual", ["Profesional", "Ceria", "Pastel Soft", "Anime"], key="p1")
    lajur = st.radio("Susunan Grid", ["1 Lajur", "2 Lajur", "Grid 2x2", "Grid 4x3"], key="p2")
    nada = st.selectbox("Nada Penulisan", ["Pendidikan", "Santai", "Inspirasi"], key="p3")

with c2:
    st.markdown("### 👥 Skop Kandungan")
    audiens = st.multiselect("Sasaran Audiens", ["Pemula", "Murid", "Guru", "Remaja"], default=["Murid"], key="p4")
    tema = st.text_input("Tema / Topik", placeholder="Cth: RBT Tahun 5", key="p5")
    format_o = st.selectbox("Format Output", ["Infografik", "Slaid", "Nota Ringkas"], key="p6")

with c3:
    st.markdown("### 💎 Butiran Visual")
    warna_s = st.selectbox("Skema Warna", ["Colorful", "Pastel", "Sejuk", "Hangat"], key="p7")
    latar_s = st.selectbox("Gaya Latar", ["Putih", "Digital", "Kertas"], key="p8")
    arahan = st.text_input("Lain-lain Arahan", placeholder="Cth: Masukkan pantun...", key="p9")

# --- BUTTON JANA ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("JANA PROMPT SEKARANG 💗"):
    st.balloons()
    hasil = f"Jana {format_o} {gaya} bertema {tema} untuk {audiens}. Nada {nada} dan warna {warna_s}."
    st.code(hasil, language="text")

st.markdown("<br><center>Disediakan oleh Cikgu Moon - SK Telok Berembang</center>", unsafe_allow_html=True)
