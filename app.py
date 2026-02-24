import streamlit as st

# Set layout wide
st.set_page_config(layout="wide")

# KOD CSS UNTUK TAJUK SAHAJA (FOKUS UTAMA)
st.markdown("""
    <style>
    /* 1. Latar Belakang Biru Laut Pastel dengan dot halus */
    .stApp {
        background-color: #E0F7FA !important;
        background-image: radial-gradient(#FFB6C1 1.5px, transparent 1.5px);
        background-size: 40px 40px;
    }

    /* 2. Container Header */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 40px;
        gap: 40px;
    }

    /* 3. TULISAN TAJUK STYLE STIKER (RE-FIXED) */
    .bubble-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 85px; 
        font-weight: 900;
        text-align: center;
        line-height: 1.2;
        
        /* Teknik Outline Putih Tebal yang tak kacau warna dalam */
        color: white; /* Ini warna outline */
        text-shadow: 
            -8px -8px 0 #fff,  
             8px -8px 0 #fff,
            -8px  8px 0 #fff,
             8px  8px 0 #fff,
             10px 10px 20px rgba(0,0,0,0.1);
        
        position: relative;
        display: inline-block;
    }

    /* Lapisan warna pelangi di atas outline */
    .bubble-title span {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(to right, #FFB6C1, #FFD700, #90EE90, #ADD8E6, #DDA0DD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        z-index: 1;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SUSUNAN HEADER ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
col_logo, col_text = st.columns([1, 4])

with col_logo:
    try:
        # Panggil logo.png Moon
        st.image("logo.png", width=300) 
    except:
        st.write("🌸")

with col_text:
    # Teknik dual-layer supaya warna pelangi tak hilang lagi
    st.markdown('''
        <h1 class="bubble-title">
            CHATBOT CIKGU MOON
            <span>CHATBOT CIKGU MOON</span>
        </h1>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.success("Bubu dah lapiskan warna pelangi tu supaya tak jadi putih kosong lagi. Cuba refresh GitHub/Streamlit Moon!")
