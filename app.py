import streamlit as st

# Set page config
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# CSS untuk memenuhi 7 point dan tema aesthetic Moon
st.markdown("""
    <style>
    /* 1. Background Biru Laut dengan corak Love/Bintang */
    .stApp {
        background-color: #E0F2F7;
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png");
    }

    /* 2. Tajuk Warna-Warni Berkilaun (Rainbow Glow) */
    .rainbow-text {
        font-family: 'Arial Black', sans-serif;
        font-size: 55px;
        text-align: center;
        background: linear-gradient(to right, #FFB6C1, #FFD700, #90EE90, #ADD8E6, #DDA0DD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(4px 4px 8px rgba(255, 255, 255, 0.8));
        font-weight: bold;
        margin-bottom: 30px;
    }

    /* 3. Kotak UI Pink Lembut & Tiada Hitam */
    div[data-baseweb="select"], div[data-baseweb="input"], .stTextArea textarea {
        background-color: #FFD1DC !important; 
        border: 2px solid #FFB6C1 !important;
        border-radius: 15px !important;
    }

    /* Warna tulisan dalam input (Coklat Lembut) */
    input, span, p, label {
        color: #7A5C61 !important;
        font-weight: bold !important;
    }

    /* 4. Button Jana yang Aesthetic */
    .stButton>button {
        background: linear-gradient(to right, #FFD1DC, #B2F2BB) !important;
        color: #7A5C61 !important;
        border: 4px solid white !important;
        border-radius: 50px !important;
        font-size: 22px !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Header Container */
    .header-box {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER (Logo Besar Sebelah Tajuk) ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png", width=200) # Saiz besar ikut kehendak Moon
    except:
        st.write("🌸")

with col_title:
    st.markdown('<h1 class="rainbow-text">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)

# --- 7 POINT UI (Ikut Rujukan Penjana Prompt) ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### ✨ Keutamaan Gaya")
    # Point 1: Gaya Visual
    gaya = st.selectbox("Gaya Visual", ["Profesional", "Ceria", "Pastel Soft", "Anime/Chibi"])
    # Point 2: Lajur/Grid
    grid = st.selectbox("Lajur atau Grid", ["1 Lajur", "2 Lajur", "Grid Panel 2x2", "Grid Panel 4x3"])
    # Point 3: Nada
    nada = st.selectbox("Nada", ["Pendidikan", "Santai", "Formal", "Inspirasi"])

with c2:
    st.markdown("### 👥 Skop Kandungan")
    # Point 4: Sasaran Audiens
    audiens = st.multiselect("Sasaran Audiens", ["Pemula", "Murid", "Guru", "Orang Awam"], default=["Murid"])
    # Point 5: Tema
    tema = st.text_input("Tema / Topik (Pilihan)", placeholder="Cth: RBT Tahun 5")
    st.selectbox("Format Output", ["Infografik", "Slaid", "Nota Ringkas"])

with c3:
    st.markdown("### 💎 Butiran Visual")
    # Point 6: Skema Warna
    warna = st.selectbox("Skema Warna", ["Colorful", "Pastel", "Sejuk", "Hangat", "Monokrom"])
    # Point 7: Latar Belakang
    latar = st.selectbox("Gaya Latar Belakang", ["Putih", "Digital", "Kertas", "Gradien"])
    st.text_input("Lain-lain Arahan", placeholder="Taip di sini...")

# --- ACTION ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("JANA PROMPT SEKARANG 💗"):
    st.balloons()
    st.success("Prompt Berjaya Dijana!")
    hasil = f"Bantu saya jana kandungan {gaya} bertemakan {tema} untuk {audiens}. Gunakan skema warna {warna}."
    st.code(hasil, language="text")

st.markdown("<br><center>Disediakan oleh Cikgu Moon - SK Telok Berembang</center>", unsafe_allow_html=True)
