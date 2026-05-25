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
            "Sate Ayam": "🍢",
            "Soto": "🥣",

            "Kentang Goreng": "🍟",
            "Cilok": "🍡",
            "Batagor": "🥟",
            "Sosis Bakar": "🌭",
            "Roti Bakar": "🍞",
            "Siomay": "🥠",
            "Dimsum": "🥢",
            "Corndog": "🧀",

            "Donat": "🍩",
            "Brownies": "🧁",
            "Es Krim": "🍦",
            "Cheesecake": "🧀",
            "Waffle": "🧇",
            "Pancake": "🥞",
            "Coklat Dubai": "🍫",

            "Thai Tea": "🥤",
            "Boba Brown Sugar": "🧋",
            "Kopi Latte": "☕",
            "Milkshake": "🥛",
            "Es Jeruk": "🍊",
            "Lemon Tea": "🍋",
            "Matcha Latte": "🍵",
            "Yakult": "🍹"
        }

kategori = {

    "Makanan Berat": [
        "Bakso",
        "Mie Ayam",
        "Nasi Goreng",
        "Ayam Geprek",
        "Burger",
        "Pizza",
        "Steak",
        "Sate Ayam",
        "Soto",
        "Sushi"
    ],

    "Makanan Ringan": [
        "Kentang Goreng",
        "Cilok",
        "Batagor",
        "Sosis Bakar",
        "Roti Bakar",
        "Siomay",
        "Dimsum",
        "Corndog"
    ],

    "Dessert": [
        "Donat",
        "Brownies",
        "Es Krim",
        "Cheesecake",
        "Waffle",
        "Pancake",
        "Coklat Dubai"
    ],

    "Minuman": [
        "Thai Tea",
        "Boba Brown Sugar",
        "Kopi Latte",
        "Milkshake",
        "Es Jeruk",
        "Lemon Tea",
        "Matcha Latte",
        "Yakult"
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
        ("Mie Ayam Pangsit", 18000),
        ("Mie Ayam Jumbo", 27000)
    ],
    "Nasi Goreng": [
        ("Nasi Goreng Seafood", 35000),
        ("Nasi Goreng Kampung", 18000),
        ("Nasi Goreng Mawut", 25000),
        ("Nasi Goreng Spesial", 30000)
    ],
    "Ayam Geprek": [
        ("Ayam Geprek Mozarella", 35000),
        ("Ayam Geprek Keju", 30000),
        ("Ayam Geprek Sambal Matah", 28000),
        ("Ayam Geprek Jumbo", 40000)
    ],
    "Burger": [
        ("Cheese Burger", 25000),
        ("Double Beef Burger", 45000),
        ("Chicken Burger", 22000),
        ("BBQ Burger", 35000)
    ],
    "Pizza": [
        ("Pizza Pepperoni", 70000),
        ("Pizza Mozarella", 80000),
        ("Pizza Supreme", 95000),
        ("Pizza Beef", 85000)
    ],
    "Steak": [
        ("Chicken Steak", 50000),
        ("Sirloin Steak", 85000),
        ("Tenderloin Steak", 120000),
        ("Wagyu Steak", 180000)
    ],
    "Sate Ayam": [
        ("Sate Ayam Madura", 25000),
        ("Sate Ayam Taichan", 30000),
        ("Sate Ayam Jumbo", 35000),
        ("Sate Ayam Pedas", 28000)
    ],
    "Soto": [
        ("Soto Ayam", 20000),
        ("Soto Lamongan", 25000),
        ("Soto Betawi", 35000),
        ("Soto Daging", 40000)
    ],
    "Sushi": [
        ("Salmon Sushi", 20000),
        ("Inari Sushi", 15000),
        ("tamago Sushi", 10000),
        ("Salmon Mentai Sushi", 25000)
    ],
    "Kentang Goreng": [
        ("French Fries BBQ", 18000),
        ("French Fries Cheese", 25000),
        ("French Fries Spicy", 20000),
        ("Loaded Fries", 35000)
    ],
    "Cilok": [
        ("Cilok Kuah", 12000),
        ("Cilok Pedas", 15000),
        ("Cilok Mozarella", 22000),
        ("Cilok Isi Ayam", 18000)
    ],
    "Batagor": [
        ("Batagor Kuah", 20000),
        ("Batagor Kering", 18000),
        ("Batagor Mozarella", 30000),
        ("Batagor Spesial", 35000)
    ],
    "Sosis Bakar": [
        ("Sosis Bakar Jumbo", 20000),
        ("Sosis Bakar BBQ", 18000),
        ("Sosis Bakar Keju", 25000),
        ("Sosis Bakar Pedas", 22000)
    ],
    "Roti Bakar": [
        ("Roti Bakar Coklat", 18000),
        ("Roti Bakar Keju", 20000),
        ("Roti Bakar Oreo", 25000),
        ("Roti Bakar Tiramisu", 28000)
    ],
    "Siomay": [
        ("Siomay Bandung", 22000),
        ("Siomay Jumbo", 28000),
        ("Siomay Pedas", 25000),
        ("Siomay Seafood", 35000)
    ],
    "Dimsum": [
        ("Dimsum Original", 18000),
        ("Dimsum Chili Oil", 22000),
        ("Dimsum Mentai", 30000),
        ("Dimsum Mozarella", 28000)
    ],
    "Corndog": [
        ("Corndog Mozarella", 25000),
        ("Corndog Sosis", 22000),
        ("Corndog Coklat", 28000),
        ("Corndog Spicy Mayo", 30000)
    ],
    "Donat": [
        ("Donat Coklat", 12000),
        ("Donat Strawberry", 15000),
        ("Donat Oreo", 18000),
        ("Donat Tiramisu", 22000)
    ],
    "Brownies": [
        ("Brownies Kukus", 25000),
        ("Brownies Lumer", 30000),
        ("Brownies Almond", 35000),
        ("Brownies Keju", 32000)
    ],
    "Es Krim": [
        ("Es Krim Vanilla", 15000),
        ("Es Krim Coklat", 18000),
        ("Es Krim Strawberry", 20000),
        ("Es Krim Matcha", 28000)
    ],
    "Cheesecake": [
        ("Cheesecake Oreo", 40000),
        ("Cheesecake Matcha", 50000),
        ("Cheesecake Strawberry", 45000),
        ("Cheesecake Blueberry", 55000)
    ],
    "Waffle": [
        ("Waffle Coklat", 25000),
        ("Waffle Strawberry", 28000),
        ("Waffle Ice Cream", 35000),
        ("Waffle Matcha", 40000)
    ],
    "Pancake": [
        ("Pancake Maple", 25000),
        ("Pancake Coklat", 28000),
        ("Pancake Strawberry", 30000),
        ("Pancake Ice Cream", 38000)
    ],
    "Coklat Dubai": [
        ("Coklat Dubai Mini", 50000),
        ("Coklat Dubai", 250000),
        ("Dubai Chewy Cookie Mini", 25000),
        ("Dubai Chewy Cookie Jumbo", 150000)
    ],
    "Thai Tea": [
        ("Thai Tea Original", 15000),
        ("Thai Tea Cheese", 25000),
        ("Thai Tea Brown Sugar", 30000),
        ("Thai Tea Jumbo", 22000)
    ],
    "Boba Brown Sugar": [
        ("Brown Sugar Fresh Milk", 30000),
        ("Brown Sugar Regal", 35000),
        ("Brown Sugar Oreo", 40000),
        ("Brown Sugar Cheese", 45000)
    ],
    "Kopi Latte": [
        ("Vanilla Latte", 30000),
        ("Hazelnut Latte", 35000),
        ("Caramel Latte", 38000),
        ("Mocha Latte", 42000)
    ],
    "Milkshake": [
        ("Chocolate Milkshake", 25000),
        ("Vanilla Milkshake", 28000),
        ("Strawberry Milkshake", 30000),
        ("Oreo Milkshake", 35000)
    ],
    "Es Jeruk": [
        ("Es Jeruk Peras", 12000),
        ("Orange Float", 25000),
        ("Es Jeruk Jumbo", 18000),
        ("Es Jeruk Nipis", 15000)
    ],
    "Lemon Tea": [
        ("Lemon Tea Original", 15000),
        ("Honey Lemon Tea", 25000),
        ("Lychee Lemon Tea", 30000),
        ("Yakult Lemon Tea", 35000)
    ],
    "Matcha Latte": [
        ("Matcha Latte Original", 35000),
        ("Creamy Matcha Latte", 45000),
        ("Premium Matcha Latte", 65000),
        ("Matcha Brown Sugar", 50000)
    ],
    "Yakult": [
        ("Yakult Strawberry", 25000),
        ("Yakult Mango", 28000),
        ("Yakult Lychee", 30000),
        ("Yakult Mix Berry", 35000)
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
        ("Double Beef Burger", 5),
        ("Premium Matcha Latte", 5),
        ("Cheesecake Blueberry", 5),
        ("Salmon Mentai Sushi",5),
        ("Dubai Chewy Cookie Jumbo",5)
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
