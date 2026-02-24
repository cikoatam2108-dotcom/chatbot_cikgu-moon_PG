import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# CSS UNTUK LAYOUT KEMAS, BACKGROUND BINTANG & TAJUK SEBELAH LOGO
st.markdown("""
    <style>
    /* 1. Background Biru Pastel dengan Corak Bintang/Love */
    .stApp {
        background-color: #E0F2F7;
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png"); /* Corak bintang halus */
    }
    
    /* 2. Header Container (Susun Logo & Tajuk Sebelah-sebelah) */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 50px;
        margin-bottom: 30px;
    }

    /* 3. Tajuk Warna-Warni (Font sebijik macam gambar) */
    .rainbow-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 50px;
        font-weight: bold;
        color: white;
        text-shadow: 
            -3px -3px 0 #FFB6C1,  
             3px -3px 0 #FFD700,
            -3px  3px 0 #90EE90,
             3px  3px 0 #ADD8E6,
             5px  5px 10px rgba(0,0,0,0.2);
    }

    /* 4. Kotak UI Pink Lembut (Lebih Kemas & Tak Bertindih) */
    .stSelectbox, .stTextInput, .stMultiSelect, div[data-baseweb="select"] {
        margin-bottom: 15px !important;
    }

    div[data-baseweb="select"], div[data-baseweb="input"], .stTextArea textarea {
        background-color: #FFD1DC !important; 
        border: 2px solid #FFB6C1 !important;
        border-radius: 20px !important;
        padding: 5px !important;
    }

    /* Label tulisan atas kotak */
    .stMarkdown p {
        color: #7A5C61 !important;
        font-weight: bold;
        font-size: 16px;
    }

    /* 5. Button Jana (Besar & Comel) */
    .stButton>button {
        background: linear-gradient(to right, #FFD1DC, #B2F2BB) !important;
        color: #555 !important;
        border-radius: 50px !important;
        border: 5px solid white !important;
        font-size: 24px !important;
        font-weight: bold !important;
        height: 70px !important;
        width: 100% !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- BAHAGIAN ATAS (LOGO + TAJUK) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
col_logo, col_text = st.columns([1, 4])

with col_logo:
    # Bubu panggil logo.png yang Moon letak kat tepi tu
    try:
        st.image("logo.png", width=120)
    except:
        st.write("🖼️") # Emoji ganti kalau logo belum upload

with col_text:
    st.markdown('<h1 class="rainbow-title">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- BAHAGIAN UTAMA (KOTAK UI PINK) ---
# Guna 4 kolum supaya nampak luas dan tak bertindih
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("### 🎨 Gaya Visual")
    gaya = st.selectbox("Gaya", ["Profesional", "Pastel Soft", "Ceria"], key="g1")
    lajur = st.selectbox("Grid", ["1 Lajur", "2 Lajur", "Grid 3x2"], key="g2")

with c2:
    st.markdown("### 👥 Audiens")
    audiens = st.selectbox("Sasaran", ["Murid", "Guru", "Ibu Papa"], key="s1")
    tema = st.text_input("Tema", placeholder="Taip di sini...", key="s2")

with c3:
    st.markdown("### 📝 Kandungan")
    jenis = st.selectbox("Output", ["Infografik", "Slaid", "Nota"], key="k1")
    nada = st.selectbox("Nada", ["Pendidikan", "Santai", "Formal"], key="k2")

with c4:
    st.markdown("### 💎 Butiran")
    warna = st.selectbox("Skema Warna", ["Gula-gula", "Sejuk", "Hangat"], key="b1")
    latar = st.selectbox("Latar", ["Putih", "Digital", "Kertas"], key="b2")

# --- BUTTON JANA ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("JANA PROMPT SEKARANG 💗"):
    st.balloons()
    st.markdown("---")
    hasil_prompt = f"Bantu saya jana {jenis} bertema {tema} untuk {audiens} dengan gaya {gaya}. Warna utama ialah {warna}."
    st.success("Siap! Salin prompt di bawah:")
    st.code(hasil_prompt, language="text")

st.markdown("<br><center>Disediakan oleh Cikgu Moon - SK Telok Berembang</center>", unsafe_allow_html=True)
