# =========================================================
# GG BITES - STREAMLIT APP
# =========================================================

import streamlit as st
import random
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="GG BITES",
    page_icon="🍽️",
    layout="wide"
)

# =========================================================
# CLASS GRAPH
# =========================================================
class GGBitesGraph:

    def __init__(self):

        self.admin_code = "GGBITES_ADMIN"
        
        self.emoji = {
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
        # =================================================
        # KATEGORI MENU
        # =================================================
        self.kategori = {
            "Makanan Berat": [
                "Bakso",
                "Mie Ayam",
                "Nasi Goreng",
                "Ayam Geprek",
                "Burger",
                "Pizza",
                "Steak",
                "Sate Ayam",
                "Soto"
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
        
        self.graph_combo = {
            "Bakso": [
                ("Es Jeruk", 5),
                ("Kentang Goreng", 4)
            ],
            "Burger": [
                ("Milkshake", 5),
                ("Kentang Goreng", 5)
            ],
            "Pizza": [
                ("Lemon Tea", 4),
                ("Kentang Goreng", 5)
            ],
            "Steak": [
                ("Cheesecake", 4),
                ("Matcha Latte", 5)
            ],
            "Donat": [
                ("Kopi Latte", 5),
                ("Thai Tea", 4)
            ],
            "Brownies": [
                ("Es Krim", 5),
                ("Kopi Latte", 5)
            ]
        }

app = GGBitesGraph()

# =========================================================
# SESSION
# =========================================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "orders" not in st.session_state:
    st.session_state.orders = []

if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

.stApp{
    background:#f8f7f4;
}

.header{
    text-align:center;
    padding:20px;
}

.title{
    font-size:55px;
    font-weight:bold;
    color:#ff4f8b;
}

.subtitle{
    font-size:22px;
    color:#666;
}

.food-card{
    background:white;
    border-radius:25px;
    padding:20px;
    text-align:center;
    margin-bottom:20px;
    height:320px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
}

.food-emoji{
    font-size:60px;
}

.food-name{
    font-size:20px;
    font-weight:bold;
    margin-top:10px;
}

.food-price{
    color:#ff4f8b;
    font-size:24px;
    font-weight:bold;
    margin-top:10px;
}

.category-title{
    font-size:35px;
    font-weight:bold;
    color:#333;
    margin-top:30px;
}

.sub-menu{
    font-size:24px;
    font-weight:bold;
    color:#ff4f8b;
    margin-top:20px;
}

.stButton>button{
    width:100%;
    background:#ff4f8b;
    color:white;
    border:none;
    border-radius:15px;
    height:45px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#ff2f74;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
col1, col2 = st.columns([6,1])

with col1:

    st.markdown("""
    <div class="header">
    <div class="title">🍔 GG BITES 🍔</div>
    <div class="subtitle">
    Smart Food Recommendation & Ordering System
    </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.write("")

    if st.button(f"🛒 {len(st.session_state.cart)}"):
        st.session_state.page = "cart"

# =========================================================
# SIDEBAR
# =========================================================
menu = st.sidebar.radio(
    "📋 MENU",
    [
        "🍔 Order Menu",
        "🍟 Combo Recommendation",
        "🍕 Top Menu",
        "🎲 Random Pick",
        "💰 Rekomendasi Harga",
        "🔍 Search Menu",
        "🔐 Admin"
    ]
)

# =========================================================
# CART PAGE
# =========================================================
if st.session_state.page == "cart":

    st.title("🛒 Keranjang Pesanan")

    total = 0

    if len(st.session_state.cart) == 0:
        st.warning("Keranjang masih kosong!")

    else:

        for i, (nama, harga) in enumerate(st.session_state.cart):

            col1, col2, col3 = st.columns([4,2,1])

            with col1:
                st.write(f"🍽 {nama}")

            with col2:
                st.write(f"Rp{harga:,}")

            with col3:

                if st.button("❌", key=f"hapus{i}"):
                    st.session_state.cart.pop(i)
                    st.rerun()

            total += harga

        st.markdown("---")

        st.subheader(f"💰 Total : Rp{total:,}")

        nama = st.text_input("Nama Pemesan")

        metode = st.selectbox(
            "Metode Pembayaran",
            ["QRIS", "Cash", "Transfer"]
        )

        if metode == "QRIS":
            st.image(
                "https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=GG-BITES"
            )

        if st.button("✅ Checkout"):

            data = {
                "nama": nama,
                "pesanan": st.session_state.cart,
                "total": total,
                "waktu": datetime.now().strftime("%H:%M:%S"),
                "metode": metode
            }

            st.session_state.orders.append(data)

            st.success("Pesanan berhasil dibuat 🍔")

            st.session_state.cart = []

    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"
        st.rerun()

# =========================================================
# ORDER MENU
# =========================================================
else:

    if menu == "🍔 Order Menu":

        for kategori, data_menu in app.kategori.items():

            st.markdown(f"""
            <div class="category-title">
            {kategori}
            </div>
            """, unsafe_allow_html=True)

            for nama_menu, daftar in data_menu.items():

                st.markdown(f"""
                <div class="sub-menu">
                {app.emoji.get(nama_menu,'🍽')} {nama_menu}
                </div>
                """, unsafe_allow_html=True)

                cols = st.columns(4)

                for i, (nama, harga) in enumerate(daftar):

                    with cols[i % 4]:

                        st.markdown(f"""
                        <div class="food-card">

                        <div class="food-emoji">
                        {app.emoji.get(nama_menu,'🍽')}
                        </div>

                        <div class="food-name">
                        {nama}
                        </div>

                        <div class="food-price">
                        Rp{harga:,}
                        </div>

                        </div>
                        """, unsafe_allow_html=True)

                        if st.button("🛒 Tambah", key=f"{nama}"):
                            st.session_state.cart.append((nama, harga))
                            st.toast(f"{nama} ditambahkan")

    elif menu == "🍟 Combo Recommendation":

        st.title("🍟 Combo Recommendation")

        cari = st.text_input("Cari menu")

        if cari:

            ditemukan = False

            for menu_combo, rekom in app.combo.items():

                if cari.lower() in menu_combo.lower():

                    ditemukan = True

                    st.subheader(menu_combo)

                    cols = st.columns(len(rekom))

                    for i, item in enumerate(rekom):

                        with cols[i]:

                            st.markdown(f"""
                            <div class="food-card">
                            <div class="food-emoji">
                            {app.emoji.get(item,'🍽')}
                            </div>
                            <div class="food-name">
                            {item}
                            </div>
                            </div>
                            """, unsafe_allow_html=True)

            if not ditemukan:
                st.error("Combo tidak ditemukan")

    elif menu == "🍕 Top Menu":

        st.title("🍕 Top Menu")

        top = [
            ("🍔", "Double Beef Burger"),
            ("🍕", "Pizza Supreme"),
            ("🥩", "Wagyu Steak"),
            ("🍵", "Premium Matcha Latte")
        ]

        cols = st.columns(4)

        for i, (emoji, nama) in enumerate(top):

            with cols[i]:

                st.markdown(f"""
                <div class="food-card">
                <div class="food-emoji">{emoji}</div>
                <div class="food-name">{nama}</div>
                <div class="food-price">BEST SELLER</div>
                </div>
                """, unsafe_allow_html=True)

    elif menu == "🎲 Random Pick":

        semua = []

        for kategori, data in app.kategori.items():
            for nama_menu, daftar in data.items():
                semua.extend(daftar)

        pick = random.choice(semua)

        st.markdown(f"""
        <div class="food-card">
        <div class="food-emoji">🎲</div>
        <div class="food-name">{pick[0]}</div>
        <div class="food-price">Rp{pick[1]:,}</div>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "💰 Rekomendasi Harga":

        pilih = st.selectbox(
            "Pilih Harga",
            ["Murah", "Sedang", "Mahal"]
        )

        semua = []

        for kategori, data in app.kategori.items():
            for nama_menu, daftar in data.items():
                semua.extend(daftar)

        hasil = []

        if pilih == "Murah":
            hasil = [x for x in semua if x[1] <= 25000]

        elif pilih == "Sedang":
            hasil = [x for x in semua if 25000 < x[1] <= 50000]

        else:
            hasil = [x for x in semua if x[1] > 50000]

        cols = st.columns(4)

        for i, (nama, harga) in enumerate(hasil):

            with cols[i % 4]:

                st.markdown(f"""
                <div class="food-card">
                <div class="food-emoji">💰</div>
                <div class="food-name">{nama}</div>
                <div class="food-price">Rp{harga:,}</div>
                </div>
                """, unsafe_allow_html=True)

    elif menu == "🔍 Search Menu":

        st.title("🔍 Search Menu")

        keyword = st.text_input("Cari makanan")

        if keyword:

            cols = st.columns(4)

            semua = []

            for kategori, data in app.kategori.items():
                for nama_menu, daftar in data.items():
                    semua.extend(daftar)

            ditemukan = False

            for i, (nama, harga) in enumerate(semua):

                if keyword.lower() in nama.lower():

                    ditemukan = True

                    with cols[i % 4]:

                        st.markdown(f"""
                        <div class="food-card">
                        <div class="food-emoji">🔍</div>
                        <div class="food-name">{nama}</div>
                        <div class="food-price">Rp{harga:,}</div>
                        </div>
                        """, unsafe_allow_html=True)

            if not ditemukan:
                st.error("Menu tidak ditemukan")

    elif menu == "🔐 Admin":

        st.title("🔐 Admin Dashboard")

        kode = st.text_input(
            "Masukkan kode admin",
            type="password"
        )

        if kode == app.admin_code:

            st.success("Login berhasil")

            total_pesanan = len(st.session_state.orders)

            total_uang = 0

            for order in st.session_state.orders:
                total_uang += order["total"]

            col1, col2 = st.columns(2)

            with col1:
                st.metric("📦 Total Pesanan", total_pesanan)

            with col2:
                st.metric("💰 Pendapatan", f"Rp{total_uang:,}")

            st.markdown("---")

            st.subheader("📋 Pesanan Masuk")

            if len(st.session_state.orders) == 0:
                st.info("Belum ada pesanan")

            else:

                for i, order in enumerate(st.session_state.orders):

                    with st.expander(f"Pesanan #{i+1}"):

                        st.write(f"👤 Nama : {order['nama']}")
                        st.write(f"🕒 Jam : {order['waktu']}")
                        st.write(f"💳 Pembayaran : {order['metode']}")

                        st.write("🍽 Pesanan :")

                        for item, harga in order["pesanan"]:
                            st.write(f"- {item} | Rp{harga:,}")

                        st.success(f"💰 Total : Rp{order['total']:,}")

        elif kode != "":
            st.error("Kode admin salah")
