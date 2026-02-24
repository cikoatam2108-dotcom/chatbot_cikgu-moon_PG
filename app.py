import streamlit as st

# 1. Setup halaman wide
st.set_page_config(layout="wide")

# 2. Kod CSS Fokus Warna Pastel & Tanpa Garisan Putih
st.markdown("""
    <style>
    /* Latar Belakang Biru Laut Pastel */
    .stApp {
        background-color: #E0F7FA !important;
        background-image: radial-gradient(#FFB6C1 1px, transparent 1px);
        background-size: 30px 30px;
    }

    /* Container Header */
    .header-box {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        gap: 30px;
    }

    /* TULISAN TAJUK - Warna Pastel Solid (Tiada Garisan Putih) */
    .pastel-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 80px;
        font-weight: bold;
        text-align: center;
        /* Warna-warni Gula-gula Pastel */
        background: linear-gradient(to right, #FF9AA2, #FFB7B2, #FFDAC1, #E2F0CB, #B5EAD7, #C7CEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        width: 100%;
        margin: 0;
    }
    
    /* Hilangkan garisan putih bawah tajuk */
    hr {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SUSUNAN HEADER ---
col1, col2 = st.columns([1, 4])

with col1:
    try:
        # Panggil logo.png Moon
        st.image("logo.png", width=300)
    except:
        st.write("🌸")

with col2:
    # Tajuk warna-warni tanpa outline putih
    st.markdown('<h1 class="pastel-title">CHATBOT CIKGU MOON</h1>', unsafe_allow_html=True)

st.write(" ")
st.info("Fokus: Warna pastel pelangi tanpa garisan putih. Dah nampak macam yang Moon nak?")
