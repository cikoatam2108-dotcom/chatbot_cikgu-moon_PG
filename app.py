import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# CSS UNTUK TEMA BIRU PASTEL + KOTAK PINK + TAJUK WARNA-WARNI
st.markdown("""
    <style>
    /* 1. Latar Belakang Biru Pastel */
    .stApp {
        background-color: #E0F2F7; 
    }
    
    /* 2. Tajuk Warna-Warni (Gradient) */
    .rainbow-text {
        font-family: 'Arial Black', sans-serif;
        font-size: 45px;
        background: linear-gradient(to right, #FFB6C1, #FFD700, #90EE90, #ADD8E6, #DDA0DD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* 3. Kotak UI Warna Pink Lembut */
    div[data-baseweb="select"], 
    div[data-baseweb="input"],
    div[data-baseweb="base-input"],
    .stMultiSelect div[data-baseweb="select"],
    .stSelectbox div, .stTextInput div {
        background-color: #FFD1DC !important; /* Pink Lembut Pastel */
        border: 2px solid #FFB6C1 !important;
        border-radius: 15px !important;
        color: #7A5C61 !important;
    }

    /* Tulisan dalam kotak input */
    input, span, p {
        color: #7A5C61 !important;
    }

    /* 4. Button Jana Prompt */
    .stButton>button {
        background-color: #B2F2BB !important; /* Hijau Pastel */
        color: #555 !important;
        border-radius: 30px !important;
        border: 4px solid #FFFFFF !important;
        font-size: 20px !important;
        font-weight: bold;
        width: 100%;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    /* 5. Gambar Logo tengah-tengah */
    .logo-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BAHAGIAN GAMBAR LOGO MOON ---
# Bubu dah masukkan logik panggil logo.png kat sini
try:
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("logo.png", width=250) # Pastikan fail kat GitHub nama dia logo.png
    st.markdown('</div>', unsafe_allow_html=True)
except:
    st.write("*(Logo Moon akan muncul kat sini bila fail logo.png dah masuk GitHub)*")

# --- TAJUK WARNA-WARNI ---
st.markdown('<h1 class="rainbow-text">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)

# --- SUSUNAN KOTAK UI PINK ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎨 Gaya Visual")
    gaya = st.selectbox("Pilih Gaya", ["Profesional", "Ceria/Anime", "Pastel Soft"], key="1")
    lajur = st.radio("Lajur atau Grid", ["1 Lajur", "2 Lajur", "Grid 2x2"], key="2")

with col2:
    st.markdown("### 👥 Sasaran")
    audiens = st.multiselect("Sasaran Audiens", ["Murid", "Guru", "Ibu bapa"], default=["Murid"], key="3")
    tema = st.text_input("Tema / Topik", placeholder="Contoh: RBT Tahun 5", key="4")

with col3:
    st.markdown("### 💎 Butiran")
    warna = st.selectbox("Skema Warna", ["Colorful", "Pastel", "Monokrom"], key="5")
    latar = st.selectbox("Gaya Latar", ["Putih", "Digital", "Buku Nota"], key="6")

st.markdown("<br>", unsafe_allow_html=True)

# --- BUTTON JANA ---
if st.button("JANA PROMPT SEKARANG 💗"):
    st.balloons()
    st.success("Prompt Berjaya Dijana!")
    hasil = f"Sila buatkan {gaya} bertemakan {tema} untuk {audiens}. Gunakan warna {warna}."
    st.code(hasil, language="text")

st.markdown("<center>Disediakan dengan ❤️ oleh Cikgu Moon</center>", unsafe_allow_html=True)
