import streamlit as st

# 1. Pastikan layout wide supaya tak bertindih
st.set_page_config(layout="wide")

# 2. KOD KHAS UNTUK TAJUK SEBIJIK MACAM GAMBAR
st.markdown("""
    <style>
    /* Background Biru Laut Pastel */
    .stApp {
        background-color: #E0F7FA !important;
        background-image: radial-gradient(#FFB6C1 1px, transparent 1px), radial-gradient(#FFD700 1px, transparent 1px);
        background-size: 40px 40px;
    }

    /* Container Tajuk & Logo */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        padding: 30px;
    }

    /* TULISAN TAJUK MACAM DALAM GAMBAR (Bubble Font Style) */
    .bubble-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 70px; /* Saiz besar */
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        /* Kesan White Outline Tebal */
        -webkit-text-stroke: 10px white; 
        paint-order: stroke fill;
        /* Warna-warni Gula-gula */
        background: linear-gradient(to right, #FF9AA2, #FFB7B2, #FFDAC1, #E2F0CB, #B5EAD7, #C7CEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        /* Bayang supaya nampak timbul */
        filter: drop-shadow(5px 5px 0px rgba(0,0,0,0.1));
    }

    /* KOTAK UI PINK (BUANG HITAM) */
    div[data-baseweb="select"], div[data-baseweb="input"], .stSelectbox div {
        background-color: #FFD1DC !important; /* Warna Pink Rujukan */
        border: 3px solid white !important;
        border-radius: 15px !important;
    }

    /* Warna Tulisan Label & Pilihan */
    label p, span, div {
        color: #7A5C61 !important; /* Coklat Pink Lembut */
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SUSUNAN HEADER ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
col_img, col_txt = st.columns([1, 4])

with col_img:
    st.image("logo.png", width=250) # Logo besar sebelah tajuk

with col_txt:
    # Tajuk yang Moon nak
    st.markdown('<h1 class="bubble-title">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7 POINT UI (IKUT RUJUKAN) ---
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### ✨ Keutamaan Gaya")
    st.selectbox("Gaya Visual", ["Profesional", "Ceria", "Pastel Soft"], key="v1")
    st.radio("Lajur atau Grid", ["1 Lajur", "2 Lajur", "Grid 2x2"], key="v2")
    st.selectbox("Nada", ["Pendidikan", "Santai"], key="v3")

with c2:
    st.markdown("### 👥 Skop Kandungan")
    st.multiselect("Sasaran Audiens", ["Murid", "Guru", "Ibu Bapa"], default=["Murid"], key="s1")
    st.text_input("Tema / Topik", placeholder="Cth: RBT Tahun 5", key="s2")

with c3:
    st.markdown("### 💎 Butiran Visual")
    st.selectbox("Skema Warna", ["Colorful", "Pastel", "Sejuk"], key="b1")
    st.selectbox("Gaya Latar Belakang", ["Putih", "Digital", "Kertas"], key="b2")

st.markdown("<br>", unsafe_allow_html=True)
st.button("JANA PROMPT SEKARANG 💗")
