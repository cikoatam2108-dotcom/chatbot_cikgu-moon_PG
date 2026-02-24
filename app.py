import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Chatbot Cikgu Moon", page_icon="🌸", layout="wide")

# CSS KHAS: TEMA PINK LEMBUT PASTEL
st.markdown("""
    <style>
    /* 1. Latar Belakang Keseluruhan (Pink Sangat Lembut) */
    .stApp {
        background-color: #FFF0F5; 
    }
    
    /* 2. Warna Teks (Kelabu Pink Lembut, Bukan Hitam) */
    html, body, [class*="st-"] {
        color: #B27081 !important; 
    }

    /* 3. Kotak Input (Semua jadi Pink Lembut) */
    div[data-baseweb="select"], 
    div[data-baseweb="input"],
    div[data-baseweb="base-input"],
    .stMultiSelect div[data-baseweb="select"] {
        background-color: #FFE4E1 !important; /* Misty Rose */
        border: 2px solid #FFC0CB !important; /* Pink Pastel Border */
        border-radius: 15px !important;
    }

    /* 4. Tajuk (Pink Pastel Manis) */
    h1, h2, h3 {
        color: #FFB6C1 !important; 
        font-family: 'Arial', sans-serif;
    }

    /* 5. Button (Kombinasi Pink & Hijau Pastel Lembut) */
    .stButton>button {
        background-color: #FFC0CB !important;
        color: white !important;
        border-radius: 25px !important;
        border: 3px solid #E0FFE0 !important; /* Border Hijau Pastel sangat lembut */
        font-weight: bold;
        padding: 10px 24px;
    }
    
    .stButton>button:hover {
        background-color: #FFD1DC !important;
        border: 3px solid #FFB6C1 !important;
    }

    /* 6. Kotak Hasil Prompt (Hijau Pastel Lembut) */
    .stCodeBlock, .stTextArea textarea {
        background-color: #F0FFF0 !important; 
        border: 2px solid #D7FFD7 !important;
        border-radius: 15px !important;
    }

    /* Hilangkan garisan fokus hitam */
    *:focus {
        outline: none !important;
        border-color: #FFB6C1 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ISI KANDUNGAN DASHBOARD ---
st.title("✨ Chatbot Cikgu Moon")
st.write("Jana prompt dengan gaya pastel yang tenang dan cantik.")

# Letak gambar Moon kat sini kalau dah ada
# st.image("logo.png", width=150)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌸 Pilihan Gaya")
    gaya = st.selectbox("Pilih Gaya Visual", ["Pastel Soft", "Ceria", "Minimalis"])
    nada = st.selectbox("Nada Suara", ["Mesra", "Pendidikan", "Santai"])

with col2:
    st.markdown("### 📝 Butiran Kandungan")
    subjek = st.text_input("Subjek/Topik", placeholder="Contoh: RBT Tahun 4")
    audiens = st.selectbox("Untuk Siapa?", ["Murid", "Guru", "Orang Awam"])

st.markdown("---")
if st.button("Jana Prompt Sekarang 💖"):
    st.success("Prompt sedang disediakan...")
    # Sini Moon boleh letak logik jana prompt macam tadi
