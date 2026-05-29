import streamlit as st
import random
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
# SESSION STATE
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
            "Burger": "🍔",
            "Pizza": "🍕",
            "Ayam Geprek": "🍗",
            "Steak": "🥩",
            "Kentang Goreng": "🍟",
            "Donat": "🍩",
            "Brownies": "🧁",
            "Boba Brown Sugar": "🧋",
            "Matcha Latte": "🍵",
            "Milkshake": "🥛",
            "Lemon Tea": "🍋",
            "Nasi Goreng": "🍚",
            "Sushi": "🍣"
        }

        # =================================================
        # GRAPH REKOMENDASI
        # =================================================
        self.graph_rekomendasi = {

            "Bakso": [
                ("Bakso Jumbo", 25000),
                ("Bakso Mercon", 22000),
                ("Bakso Urat", 18000)
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

            "Donat": [
                ("Donat Coklat", 12000),
                ("Donat Oreo", 18000),
                ("Donat Tiramisu", 22000)
            ],

            "Brownies": [
                ("Brownies Almond", 35000),
                ("Brownies Keju", 32000),
                ("Brownies Lumer", 30000)
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
            ],

            "Nasi Goreng": [
                ("Nasi Goreng Seafood", 35000),
                ("Nasi Goreng Mawut", 25000),
                ("Nasi Goreng Kampung", 18000)
            ],

            "Sushi": [
                ("Salmon Sushi", 25000),
                ("Tamago Sushi", 18000),
                ("Mentai Sushi", 35000)
            ]
        }

        # =================================================
        # GRAPH COMBO
        # =================================================
        self.graph_combo = {

            "Burger": [
                ("Kentang Goreng", 5),
                ("Milkshake", 5)
            ],

            "Pizza": [
                ("Lemon Tea", 4),
                ("Kentang Goreng", 5)
            ],

            "Donat": [
                ("Matcha Latte", 5),
                ("Milkshake", 4)
            ],

            "Bakso": [
                ("Lemon Tea", 4),
                ("Kentang Goreng", 5)
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

.food-card{
    background:white;
    padding:25px;
    border-radius:25px;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
    transition:0.3s;
}

.food-card:hover{
    transform:translateY(-5px);
}

.price{
    color:#ff5f99;
    font-size:24px;
    font-weight:bold;
}

.box{
    background:white;
    padding:20px;
    border-radius:25px;
    margin-bottom:20px;
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
# SIDEBAR
# =========================================================
menu = st.sidebar.radio(

    "📋 MENU",

    [
        "🍽️ Menu",
        "🔍 Cari Rekomendasi",
        "⭐ Top Rating",
        "💡 Combo Recommendation",
        "🎲 Random Pick",
        "💰 Rekomendasi Harga",
        "🛒 Cart",
        "🔐 Admin"
    ]
)

# =========================================================
# MENU MAKANAN
# =========================================================
if menu == "🍽️ Menu":

    st.markdown("## 🍽️ Daftar Menu")

    cols = st.columns(3)

    nomor = 0

    for menu_utama, daftar in app.graph_rekomendasi.items():

        for nama, harga in daftar:

            with cols[nomor % 3]:

                st.markdown(f"""
                <div class="food-card">
                <h1>{app.emoji.get(menu_utama,"🍽️")}</h1>
                <h2>{nama}</h2>
                <p class="price">
                Rp{harga:,}
                </p>
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"Tambah {nama}"):

                    st.session_state.cart.append({

                        "nama": nama,
                        "harga": harga
                    })

                    st.success(f"{nama} masuk cart!")

            nomor += 1

# =========================================================
# SEARCH
# =========================================================
elif menu == "🔍 Cari Rekomendasi":

    st.markdown("## 🔍 Cari Rekomendasi")

    search = st.text_input(
        "Cari menu favorit..."
    )

    if search:

        ditemukan = False

        for menu_utama, daftar in app.graph_rekomendasi.items():

            if search.lower() in menu_utama.lower():

                ditemukan = True

                st.subheader(f"✨ {menu_utama}")

                cols = st.columns(3)

                for i, (nama, harga) in enumerate(daftar):

                    with cols[i % 3]:

                        st.markdown(f"""
                        <div class="food-card">
                        <h1>{app.emoji.get(menu_utama,"🍽️")}</h1>
                        <h3>{nama}</h3>
                        <p class="price">
                        Rp{harga:,}
                        </p>
                        </div>
                        """, unsafe_allow_html=True)

        if not ditemukan:
            st.error("❌ Menu tidak ditemukan")

# =========================================================
# TOP RATING
# =========================================================
elif menu == "⭐ Top Rating":

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
            <h2>{item}</h2>
            ⭐⭐⭐⭐⭐
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# COMBO RECOMMENDATION
# =========================================================
elif menu == "💡 Combo Recommendation":

    st.markdown("## 💡 Combo Recommendation")

    for makanan, combo in app.graph_combo.items():

        st.markdown(f"""
        <div class="box">
        <h2>{app.emoji.get(makanan,"🍽️")} {makanan}</h2>
        """, unsafe_allow_html=True)

        for item, rating in combo:

            st.write(
                f"✨ {item} | {'⭐' * rating}"
            )

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RANDOM PICK
# =========================================================
elif menu == "🎲 Random Pick":

    st.markdown("## 🎲 Random Pick")

    semua_menu = []

    for daftar in app.graph_rekomendasi.values():
        semua_menu.extend(daftar)

    pick = random.choice(semua_menu)

    st.markdown(f"""
    <div class="food-card">
    <h1>🎲</h1>
    <h2>{pick[0]}</h2>
    <p class="price">
    Rp{pick[1]:,}
    </p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# REKOMENDASI HARGA
# =========================================================
elif menu == "💰 Rekomendasi Harga":

    st.markdown("## 💰 Rekomendasi Harga")

    pilihan = st.radio(

        "Pilih Harga",

        [
            "Murah",
            "Sedang",
            "Mahal"
        ]
    )

    semua = []

    for daftar in app.graph_rekomendasi.values():
        semua.extend(daftar)

    if pilihan == "Murah":

        hasil = [
            x for x in semua if x[1] <= 25000
        ]

    elif pilihan == "Sedang":

        hasil = [
            x for x in semua if 25000 < x[1] <= 50000
        ]

    else:

        hasil = [
            x for x in semua if x[1] > 50000
        ]

    cols = st.columns(3)

    for i, (nama, harga) in enumerate(hasil):

        with cols[i % 3]:

            st.markdown(f"""
            <div class="food-card">
            <h2>{nama}</h2>
            <p class="price">
            Rp{harga:,}
            </p>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# CART
# =========================================================
elif menu == "🛒 Cart":

    st.markdown("## 🛒 Pesanan Kamu")

    if len(st.session_state.cart) == 0:

        st.warning("Belum ada pesanan")

    else:

        total = 0

        for item in st.session_state.cart:

            st.markdown(f"""
            <div class="box">
            🍽️ {item['nama']}
            <br>
            💰 Rp{item['harga']:,}
            </div>
            """, unsafe_allow_html=True)

            total += item["harga"]

        st.subheader(f"💰 Total : Rp{total:,}")

        nama = st.text_input("Nama Pemesan")

        pembayaran = st.selectbox(

            "Metode Pembayaran",

            [
                "QRIS",
                "Cash",
                "DANA",
                "OVO",
                "GoPay"
            ]
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

# =========================================================
# ADMIN
# =========================================================
elif menu == "🔐 Admin":

    st.markdown("## 🔐 Admin Dashboard")

    admin = st.text_input(

        "Masukkan Kode Admin",
        type="password"
    )

    # =====================================================
    # KODE ADMIN
    # =====================================================
    # GGBITES123

    if admin == "GGBITES123":

        st.success("✅ Login Admin Berhasil")

        if len(st.session_state.orders) == 0:

            st.info("Belum ada pesanan")

        else:

            for i, order in enumerate(
                st.session_state.orders,
                start=1
            ):

                st.markdown(f"""
                <div class="box">
                <h3>📦 Order #{i}</h3>

                👤 {order['nama']} <br>
                💳 {order['pembayaran']} <br>
                💰 Rp{order['total']:,} <br>
                🕒 {order['waktu']}
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
