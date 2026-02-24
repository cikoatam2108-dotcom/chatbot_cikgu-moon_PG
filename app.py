import streamlit as st

# Set layout wide
st.set_page_config(layout="wide")

# KOD CSS UNTUK TAJUK SAHAJA (FOKUS UTAMA)
st.markdown("""
    <style>
    /* 1. Latar Belakang Biru Laut Pastel */
    .stApp {
        background-color: #E0F7FA !important;
        background-image: radial-gradient(#FFB6C1 1px, transparent 1px), radial-gradient(#FFD700 1px, transparent 1px);
        background-size: 40px 40px;
    }

    /* 2. Container Header */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 40px;
        gap: 30px;
    }

    /* 3. TULISAN TAJUK STYLE BUBBLE/STICKER (Sebijik Macam Gambar) */
    .bubble-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 80px; /* Saiz besar dan jelas */
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        
        /* Kesan White Outline Tebal (Sticker Effect) */
        -webkit-text-stroke: 12px white; 
        paint-order: stroke fill;
        
        /* Warna-warni Gula-gula Pastel */
        background: linear-gradient(to right, #FF9AA2, #FFB7B2, #FFDAC1, #E2F0CB, #B5EAD7, #C7CEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        
        /* Bayang lembut supaya nampak timbul dari background */
        filter: drop-shadow(6px 6px 0px rgba(0,0,0,0.1));
    }
    </style>
    """, unsafe_allow_html=True)

# --- SUSUNAN HEADER (LOGO SEBELAH TAJUK) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
col_logo, col_text = st.columns([1, 4])

with col_logo:
    # Saiz logo dibesarkan supaya seimbang dengan tajuk
    try:
        st.image("logo.png", width=280) 
    except:
        st.write("🌸")

with col_text:
    # Fokus Utama: Tulisan Tajuk Moon
    st.markdown('<h1 class="bubble-title">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Bahagian bawah ni Bubu biar kosong dulu supaya Moon tak serabut
st.write("---")
st.info("Fokus: Settlekan tajuk dulu bagi cantik. Amacam Moon, tulisan ni dah okay?")
