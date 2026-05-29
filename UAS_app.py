import streamlit as st
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="GG BITES",
    page_icon="💖",
    layout="wide"
)

# =========================================================
# SESSION
# =========================================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "orders" not in st.session_state:
    st.session_state.orders = []

# =========================================================
# CLASS GRAPH
# =========================================================
class GGBitesGraph:

    def __init__(self):

        self.emoji = {

            "Bakso": "🍜",
            "Nasi Goreng": "🍚",
            "Burger": "🍔",
            "Pizza": "🍕",
            "Ayam Geprek": "🍗",
            "Steak": "🥩",
            "Kentang Goreng": "🍟",
            "Boba Brown Sugar": "🧋",
            "Matcha Latte": "🍵",
            "Milkshake": "🥛"
        }

        self.graph_rekomendasi = {

            "Bakso": [
                ("Bakso Jumbo", 25000),
                ("Bakso Mercon", 22000),
                ("Bakso Urat", 18000)
            ],

            "Nasi Goreng": [
                ("Nasi Goreng Seafood", 35000),
                ("Nasi Goreng Mawut", 25000),
                ("Nasi Goreng Kampung", 18000)
            ],

            "Burger": [
                ("Cheese Burger", 25000),
                ("Double Beef Burger", 45000),
                ("Chicken Burger", 22000)
            ],

            "Pizza": [
                ("Pizza Supreme", 95000),
                ("Pizza Beef", 85000),
                ("Pizza Pepperoni", 70000)
            ],

            "Ayam Geprek": [
                ("Ayam Geprek Mozarella", 35000),
                ("Ayam Geprek Sambal Matah", 28000),
                ("Ayam Geprek Keju", 30000)
            ],

            "Steak": [
                ("Chicken Steak", 50000),
                ("Sirloin Steak", 85000),
                ("Wagyu Steak", 180000)
            ],

            "Kentang Goreng": [
                ("French Fries BBQ", 18000),
                ("Loaded Fries", 35000),
                ("French Fries Cheese", 25000)
            ],

            "Boba Brown Sugar": [
                ("Brown Sugar Regal", 35000),
                ("Brown Sugar Oreo", 40000),
                ("Brown Sugar Fresh Milk", 30000)
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
# OBJECT
# =========================================================
app = GGBitesGraph()

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom right,#fffdf8,#f5efe8);
    font-family:'Poppins',sans-serif;
}

.main-title{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#ff5f99;
}

.sub-title{
    text-align:center;
    font-size:22px;
    color:#666;
    margin-bottom:30px;
}

.box{
    background:white;
    padding:20px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.food-card{
    background:white;
    padding:25px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
    transition:0.3s;
}

.food-card:hover{
    transform:translateY(-5px);
}

.price{
    color:#ff5f99;
    font-weight:bold;
    font-size:25px;
}

.cart-box{
    background:white;
    padding:25px;
    border-radius:25px;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
}

.stButton > button{
    width:100%;
    border:none;
    border-radius:15px;
    background:linear-gradient(90deg,#ff8fb1,#ff6f91);
    color:white;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="main-title">
💖 GG BITES 💖
</div>

<div class="sub-title">
Smart Food Recommendation & Ordering System
</div>
""", unsafe_allow_html=True)

# =========================================================
# TOP MENU
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="box">
    🍽️ Menu
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="box">
    ⭐ Top Rating
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="box">
    🛒 Cart ({len(st.session_state.cart)})
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="box">
    🔐 Admin
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# SEARCH
# =========================================================
st.markdown("## 🔍 Cari Rekomendasi")

search = st.text_input(
    "Cari menu favoritmu..."
)

# =========================================================
# HASIL SEARCH
# =========================================================
if search:

    ditemukan = False

    for menu, daftar in app.graph_rekomendasi.items():

        if search.lower() in menu.lower():

            ditemukan = True

            st.subheader(f"✨ {menu}")

            cols = st.columns(3)

            for i, (nama, harga) in enumerate(daftar):

                with cols[i % 3]:

                    st.markdown(f"""
                    <div class="food-card">
                    <h1>{app.emoji.get(menu,"🍽️")}</h1>
                    <h3>{nama}</h3>
                    <p class="price">
                    Rp{harga:,}
                    </p>
                    </div>
                    """, unsafe_allow_html=True)

                    # AUTO MASUK CART
                    st.session_state.cart.append({
                        "nama": nama,
                        "harga": harga
                    })

    if not ditemukan:
        st.error("❌ Menu tidak ditemukan")

# =========================================================
# MENU UTAMA
# =========================================================
st.markdown("## 🍽️ Menu Makanan")

all_menu = []

for daftar in app.graph_rekomendasi.values():
    all_menu.extend(daftar)

cols = st.columns(3)

nomor = 0

for menu, daftar in app.graph_rekomendasi.items():

    for nama, harga in daftar:

        with cols[nomor % 3]:

            st.markdown(f"""
            <div class="food-card">
            <h1>{app.emoji.get(menu,"🍽️")}</h1>
            <h2>{nama}</h2>
            <p class="price">
            Rp{harga:,}
            </p>
            </div>
            """, unsafe_allow_html=True)

            # KLIK LANGSUNG TAMBAH
            if st.button(f"Tambah {nama}"):

                st.session_state.cart.append({
                    "nama": nama,
                    "harga": harga
                })

                st.success(f"{nama} masuk keranjang")

        nomor += 1

# =========================================================
# CART
# =========================================================
st.markdown("## 🛒 Pesanan Kamu")

st.markdown('<div class="cart-box">', unsafe_allow_html=True)

if len(st.session_state.cart) == 0:

    st.warning("Belum ada pesanan")

else:

    total = 0

    for item in st.session_state.cart:

        st.write(f"🍽️ {item['nama']} - Rp{item['harga']:,}")

        total += item["harga"]

    st.markdown("---")

    st.subheader(f"💰 Total : Rp{total:,}")

    nama = st.text_input("Nama Pemesan")

    pembayaran = st.selectbox(
        "Metode Pembayaran",
        ["QRIS", "Cash", "OVO", "DANA", "GoPay"]
    )

    if st.button("Checkout"):

        data_order = {

            "nama": nama,
            "pesanan": st.session_state.cart,
            "total": total,
            "pembayaran": pembayaran,
            "waktu": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        st.session_state.orders.append(data_order)

        st.success("✅ Pesanan berhasil dibuat!")

        st.balloons()

        st.session_state.cart = []

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# TOP RATING
# =========================================================
st.markdown("## ⭐ Top Rating")

top_rating = [
    "Wagyu Steak",
    "Pizza Supreme",
    "Premium Matcha Latte",
    "Double Beef Burger"
]

cols = st.columns(4)

for i, item in enumerate(top_rating):

    with cols[i]:

        st.markdown(f"""
        <div class="box">
        <h3>{item}</h3>
        ⭐⭐⭐⭐⭐
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ADMIN
# =========================================================
st.markdown("## 🔐 Admin Dashboard")

admin = st.text_input(
    "Masukkan Kode Admin",
    type="password"
)

# KODE ADMIN
# =========================
# GGBITES123
# =========================

if admin == "GGBITES123":

    st.success("✅ Admin berhasil login")

    if len(st.session_state.orders) == 0:

        st.info("Belum ada pesanan")

    else:

        for i, order in enumerate(st.session_state.orders, start=1):

            st.markdown(f"""
            <div class="cart-box">
            <h3>📦 Order #{i}</h3>
            <p>👤 Nama : {order['nama']}</p>
            <p>💳 Pembayaran : {order['pembayaran']}</p>
            <p>💰 Total : Rp{order['total']:,}</p>
            <p>🕒 Waktu : {order['waktu']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.write("### 🍽️ Detail Pesanan")

            for item in order["pesanan"]:

                st.write(
                    f"- {item['nama']} | Rp{item['harga']:,}"
                )

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<br><br>
<center>
💖 GG BITES © 2026
</center>
""", unsafe_allow_html=True)
