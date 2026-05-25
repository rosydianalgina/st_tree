import streamlit as st
import random

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="GG BITES",
    page_icon="💖",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(to bottom right, #fff0f6, #ffe4ef);
}

/* =========================
HEADER
========================= */
.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: bold;
    color: #ff4f9a;
    text-shadow: 3px 3px 12px rgba(255,105,180,0.4);
}

.sub-title {
    text-align: center;
    color: #555;
    font-size: 24px;
    margin-bottom: 35px;
}

/* =========================
CARD
========================= */
.card {
    background: white;
    padding: 22px;
    border-radius: 24px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(255,105,180,0.15);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(255,105,180,0.3);
}

/* =========================
MENU BOX
========================= */
.menu-box {
    background: linear-gradient(135deg, #ff66a6, #ff85c1);
    color: white;
    padding: 18px;
    border-radius: 22px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 15px;
    box-shadow: 0 5px 18px rgba(255,105,180,0.3);
}

/* =========================
BUTTON
========================= */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #ff5fa2, #ff8dc2);
    color: white;
    border: none;
    border-radius: 18px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #ff8dc2, #ff5fa2);
}

/* =========================
SIDEBAR
========================= */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #ffe0ef, #fff5fa);
}

/* =========================
INPUT
========================= */
.stTextInput input {
    border-radius: 15px;
    border: 2px solid pink;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 15px;
}

/* =========================
PRICE CARD
========================= */
.price-cheap {
    background: linear-gradient(135deg, #71e6a8, #43cc8a);
    color: white;
    padding: 20px;
    border-radius: 22px;
    margin-bottom: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.15);
}

.price-medium {
    background: linear-gradient(135deg, #6ab7ff, #4f92ff);
    color: white;
    padding: 20px;
    border-radius: 22px;
    margin-bottom: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.15);
}

.price-expensive {
    background: linear-gradient(135deg, #d68cff, #b15cff);
    color: white;
    padding: 20px;
    border-radius: 22px;
    margin-bottom: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.15);
}

/* =========================
FOOTER
========================= */
.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA MENU
# =========================================================
emoji = {
    "Bakso": "🍜",
    "Mie Ayam": "🍜",
    "Nasi Goreng": "🍚",
    "Ayam Geprek": "🍗",
    "Burger": "🍔",
    "Pizza": "🍕",
    "Steak": "🥩",
    "Dimsum": "🥢",
    "Donat": "🍩",
    "Thai Tea": "🧋",
    "Matcha Latte": "🍵",
    "Milkshake": "🥛"
}

kategori = {

    "Makanan Berat": [
        "Bakso",
        "Mie Ayam",
        "Nasi Goreng",
        "Ayam Geprek",
        "Burger",
        "Pizza",
        "Steak"
    ],

    "Makanan Ringan": [
        "Dimsum"
    ],

    "Dessert": [
        "Donat"
    ],

    "Minuman": [
        "Thai Tea",
        "Matcha Latte",
        "Milkshake"
    ]
}

graph_rekomendasi = {

    "Bakso": [
        ("Bakso Urat", 18000),
        ("Bakso Jumbo", 25000),
        ("Bakso Mercon", 22000),
        ("Bakso Halus", 17000)
    ],

    "Mie Ayam": [
        ("Mie Ayam Bakso", 20000),
        ("Mie Ayam Ceker", 23000),
        ("Mie Ayam Jumbo", 27000)
    ],

    "Nasi Goreng": [
        ("Nasi Goreng Seafood", 35000),
        ("Nasi Goreng Kampung", 18000),
        ("Nasi Goreng Mawut", 25000)
    ],

    "Ayam Geprek": [
        ("Ayam Geprek Mozarella", 35000),
        ("Ayam Geprek Sambal Matah", 28000),
        ("Ayam Geprek Jumbo", 40000)
    ],

    "Burger": [
        ("Cheese Burger", 25000),
        ("Double Beef Burger", 45000),
        ("BBQ Burger", 35000)
    ],

    "Pizza": [
        ("Pizza Pepperoni", 70000),
        ("Pizza Mozarella", 80000),
        ("Pizza Supreme", 95000)
    ],

    "Steak": [
        ("Chicken Steak", 50000),
        ("Sirloin Steak", 85000),
        ("Wagyu Steak", 180000)
    ],

    "Dimsum": [
        ("Dimsum Original", 18000),
        ("Dimsum Chili Oil", 22000),
        ("Dimsum Mentai", 30000)
    ],

    "Donat": [
        ("Donat Coklat", 12000),
        ("Donat Oreo", 18000),
        ("Donat Tiramisu", 22000)
    ],

    "Thai Tea": [
        ("Thai Tea Original", 15000),
        ("Thai Tea Brown Sugar", 30000),
        ("Thai Tea Jumbo", 22000)
    ],

    "Matcha Latte": [
        ("Premium Matcha Latte", 65000),
        ("Creamy Matcha Latte", 45000),
        ("Matcha Brown Sugar", 50000)
    ],

    "Milkshake": [
        ("Chocolate Milkshake", 25000),
        ("Vanilla Milkshake", 28000),
        ("Oreo Milkshake", 35000)
    ]
}

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="main-title">
💖 GG BITES 💖
</div>

<div class="sub-title">
Smart Food Recommendation System 🍔🍕🍜
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
menu = st.sidebar.radio(
    "📋 MENU",
    [
        "🏠 Home",
        "📖 Lihat Menu",
        "🔍 Cari Rekomendasi",
        "🔥 Favorit Hari Ini",
        "🏆 Top Rating",
        "🎲 Random Pick",
        "🔎 Search Menu",
        "💰 Rekomendasi Harga"
    ]
)

# =========================================================
# HOME
# =========================================================
if menu == "🏠 Home":

    st.markdown("""
    <div class="card">
        <h2 style="color:#ff4f9a;">💕 Selamat Datang di GG BITES</h2>
        <p style="font-size:18px;">
        Cari makanan favoritmu dengan tampilan modern dan rekomendasi terbaik setiap hari ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="menu-box">
        🍜 100+ Menu
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="menu-box">
        ⭐ Top Rating
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="menu-box">
        💖 Best Recommendation
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# LIHAT MENU
# =========================================================
elif menu == "📖 Lihat Menu":

    st.header("📖 Daftar Menu")

    for kat, daftar in kategori.items():

        st.subheader(f"🍽️ {kat}")

        cols = st.columns(2)

        for i, item in enumerate(daftar):

            icon = emoji.get(item, "🍽️")

            cols[i % 2].markdown(f"""
            <div class="card">
            <h3>{icon} {item}</h3>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# CARI REKOMENDASI
# =========================================================
elif menu == "🔍 Cari Rekomendasi":

    st.header("🔍 Cari Rekomendasi")

    kategori_pilih = st.selectbox(
        "Pilih Kategori",
        list(kategori.keys())
    )

    menu_pilih = st.selectbox(
        "Pilih Menu",
        kategori[kategori_pilih]
    )

    if st.button("✨ Tampilkan Rekomendasi"):

        hasil = graph_rekomendasi.get(menu_pilih, [])

        st.subheader(f"✨ Rekomendasi {menu_pilih}")

        cols = st.columns(2)

        for i, (nama, harga) in enumerate(hasil):

            cols[i % 2].markdown(f"""
            <div class="card">
            <h3>🍽️ {nama}</h3>
            <h2 style="color:#ff4f9a;">💰 Rp{harga:,}</h2>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# FAVORIT HARI INI
# =========================================================
elif menu == "🔥 Favorit Hari Ini":

    st.header("🔥 Favorit Hari Ini")

    semua = []

    for daftar in graph_rekomendasi.values():
        semua.extend(daftar)

    favorit = random.sample(semua, 5)

    for nama, harga in favorit:

        st.markdown(f"""
        <div class="card">
        <h3>🍽️ {nama}</h3>
        <h2 style="color:#ff4f9a;">💰 Rp{harga:,}</h2>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TOP RATING
# =========================================================
elif menu == "🏆 Top Rating":

    st.header("🏆 Top Rating")

    top_menu = [
        ("Wagyu Steak", 5),
        ("Pizza Supreme", 5),
        ("Premium Matcha Latte", 5),
        ("Double Beef Burger", 5)
    ]

    for nama, rating in top_menu:

        st.markdown(f"""
        <div class="card">
        <h3>🍽️ {nama}</h3>
        <h2 style="color:gold;">{"⭐" * rating}</h2>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# RANDOM PICK
# =========================================================
elif menu == "🎲 Random Pick":

    st.header("🎲 Random Pick")

    semua = []

    for daftar in graph_rekomendasi.values():
        semua.extend(daftar)

    pick = random.choice(semua)

    st.markdown(f"""
    <div class="card">
    <h2>🍽️ {pick[0]}</h2>
    <h1 style="color:#ff4f9a;">💰 Rp{pick[1]:,}</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# SEARCH MENU
# =========================================================
elif menu == "🔎 Search Menu":

    st.header("🔎 Search Menu")

    keyword = st.text_input("Cari menu")

    if keyword:

        ditemukan = False

        for daftar in graph_rekomendasi.values():

            for nama, harga in daftar:

                if keyword.lower() in nama.lower():

                    ditemukan = True

                    st.markdown(f"""
                    <div class="card">
                    <h3>🍽️ {nama}</h3>
                    <h2 style="color:#ff4f9a;">💰 Rp{harga:,}</h2>
                    </div>
                    """, unsafe_allow_html=True)

        if not ditemukan:
            st.error("❌ Menu tidak ditemukan!")

# =========================================================
# REKOMENDASI BERDASARKAN HARGA
# =========================================================
elif menu == "💰 Rekomendasi Harga":

    st.header("💰 Rekomendasi Berdasarkan Harga")

    pilihan = st.radio(
        "Pilih Kategori Harga",
        ["Murah", "Sedang", "Mahal"]
    )

    semua = []

    for daftar in graph_rekomendasi.values():
        semua.extend(daftar)

    if pilihan == "Murah":

        hasil = [x for x in semua if x[1] <= 25000]

        style_class = "price-cheap"

    elif pilihan == "Sedang":

        hasil = [x for x in semua if 25000 < x[1] <= 50000]

        style_class = "price-medium"

    else:

        hasil = [x for x in semua if x[1] > 50000]

        style_class = "price-expensive"

    cols = st.columns(2)

    for i, (nama, harga) in enumerate(hasil):

        cols[i % 2].markdown(f"""
        <div class="{style_class}">
        <h2>🍽️ {nama}</h2>
        <h1>💰 Rp{harga:,}</h1>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
💖 GG BITES © 2026 | Made With Streamlit
</div>
""", unsafe_allow_html=True)
