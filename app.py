import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# CSS UNTUK TEMA PASTEL PERFECT MOON
st.markdown("""
    <style>
    /* 1. Background Biru Laut dengan Corak Bintang & Love */
    .stApp {
        background-color: #E0F7FA !important;
        background-image: 
            radial-gradient(circle, #FFB6C1 10%, transparent 10.2%), 
            radial-gradient(circle, #FFD700 10%, transparent 10.2%);
        background-size: 60px 60px;
        background-position: 0 0, 30px 30px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* 2. Header Container (Logo + Tajuk) */
    .header-section {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        padding: 20px;
        margin-bottom: 30px;
    }

    .rainbow-text {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 50px;
        font-weight: bold;
        background: linear-gradient(to right, #FF9AA2, #FFB7B2, #FFDAC1, #E2F0CB, #B5EAD7, #C7CEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(3px 3px 0px white);
    }

    /* 3. Kotak Borang (UI mengikut rujukan Moon) */
    .form-container {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 25px;
        padding: 25px;
        border: 2px solid #FFD1DC;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    }

    /* 4. Kotak Input Pink Lembut */
    div[data-baseweb="select"], div[data-baseweb="input"], .stTextArea textarea {
        background-color: #FFF0F5 !important; /* Pink sangat lembut */
        border: 2px solid #FFD1DC !important;
        border-radius: 12px !important;
    }

    /* Warna tulisan dalam input (bukan hitam pekat) */
    input, span, p, label {
        color: #7A5C61 !important;
        font-weight: 500 !important;
    }

    /* 5. Button Jana (Cantik & Pastel) */
    .stButton>button {
        background: linear-gradient(to right, #FFD1DC, #B2F2BB) !important;
        color: #7A5C61 !important;
        border: 4px solid white !important;
        border-radius: 30px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        width: 100%;
        padding: 15px !important;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(255, 182, 193, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="header-section">', unsafe_allow_html=True)
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png", width=140)
    except:
        st.write("🌸")
with col_title:
    st.markdown('<h1 class="rainbow-text">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- UI BORANG (IKUT RUJUKAN GAMBAR MOON) ---
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # Lajur mengikut rujukan: Keutamaan Gaya | Skop Kandungan | Butiran
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### ✨ Keutamaan Gaya")
        gaya_v = st.selectbox("Gaya Visual", ["Profesional", "Ceria", "Minimalis", "Anime/Chibi"])
        lajur_v = st.radio("Susunan Grid", ["1 Lajur", "2 Lajur", "Grid Panel 2x2", "Grid Panel 4x3"])
        nada_v = st.selectbox("Nada", ["Pendidikan", "Santai", "Formal", "Inspirasi"])

    with c2:
        st.markdown("### 👥 Skop Kandungan")
        audiens = st.multiselect("Sasaran Audiens", ["Pemula", "Murid", "Guru", "Remaja", "Ibu Bapa"], default=["Murid"])
        tema = st.text_input("Tema / Topik (Pilihan)", placeholder="Taip di sini...")
        format_o = st.selectbox("Format Output", ["Infografik", "Slaid", "Nota Ringkas"])

    with c3:
        st.markdown("### 💎 Butiran Visual")
        skema_w = st.selectbox("Skema Warna", ["Colorful", "Pastel", "Monokrom", "Hangat/Sejuk"])
        latar_b = st.selectbox("Gaya Latar Belakang", ["Putih", "Digital", "Buku Nota", "Gradien"])
        tambahan = st.text_input("Lain-lain Arahan", placeholder="Cth: Masukkan pantun...")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Button Jana Prompt
    if st.button("JANA PROMPT SEKARANG 💗"):
        st.balloons()
        st.markdown("---")
        prompt_final = f"""
        Bantu saya sebagai {audiens}. Jana {format_o} dengan tema {tema}. 
        Gaya visual adalah {gaya_v} menggunakan warna {skema_w}. 
        Nada penulisan mestilah {nada_v} dalam Bahasa Melayu.
        """
        st.success("Prompt Berjaya Dijana!")
        st.code(prompt_final, language="text")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><center><p style='color: #B27081;'>Disediakan oleh Cikgu Moon • SK Telok Berembang</p></center>", unsafe_allow_html=True)
