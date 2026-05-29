import streamlit as st
import random
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="GG BITES",
    page_icon="🍔",
    layout="wide"
)

# =========================================================
# CLASS GRAPH
# =========================================================
class GGBitesGraph:

    def __init__(self):

        self.admin_code = "GGBITES_ADMIN"

        # =====================================================
        # EMOJI
        # =====================================================
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
            "Cheesecake": "🍰",
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

        # =====================================================
        # KATEGORI
        # =====================================================
        self.kategori = {

            "🍔 Makanan Berat": {
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
                ]
            },

            "🍟 Makanan Ringan": {

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
                ]
            },

            "🍰 Dessert": {

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
                ]
            },

            "🥤 Minuman": {

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
                ]
            }
        }

        # =====================================================
        # COMBO
        # =====================================================
        self.combo = {
            "Burger": ["Milkshake", "Kentang Goreng"],
            "Pizza": ["Lemon Tea", "Kentang Goreng"],
            "Bakso": ["Es Jeruk", "Cilok"],
            "Steak": ["Matcha Latte", "Cheesecake"]
        }

app = GGBitesGraph()

# =========================================================
# SESSION
# =========================================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "orders" not in st.session_state:
    st.session_state.orders = []

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

.stApp{
    background-color:#f8f6f2;
}

/* HEADER */

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

/* CARD */

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

/* CART */

.cart-box{
    background:white;
    padding:20px;
    border-radius:25px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
}

/* BUTTON */

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
st.markdown("""
<div class="header">
<div class="title">🍔 GG BITES 🍔</div>
<div class="subtitle">
Smart Food Recommendation & Ordering System
</div>
</div>
""", unsafe_allow_html=True)

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
# ORDER MENU
# =========================================================
if menu == "🍔 Order Menu":

    col1, col2 = st.columns([4,1])

    with col1:

        for kategori, data_menu in app.kategori.items():

            st.markdown(f"""
            <div class="category-title">{kategori}</div>
            """, unsafe_allow_html=True)

            for nama_menu, daftar in data_menu.items():

                st.markdown(f"""
                <div class="sub-menu">
                {app.emoji.get(nama_menu,"🍽")} {nama_menu}
                </div>
                """, unsafe_allow_html=True)

                cols = st.columns(4)

                for i, (nama, harga) in enumerate(daftar):

                    with cols[i % 4]:

                        st.markdown(f"""
                        <div class="food-card">
                        <div class="food-emoji">
                        {app.emoji.get(nama_menu,"🍽")}
                        </div>

                        <div class="food-name">
                        {nama}
                        </div>

                        <div class="food-price">
                        Rp{harga:,}
                        </div>
                        </div>
                        """, unsafe_allow_html=True)

                        if st.button(
                            f"🛒 Tambah",
                            key=f"{nama}"
                        ):
                            st.session_state.cart.append((nama, harga))
                            st.toast(f"{nama} ditambahkan 🛒")

    # =====================================================
    # CART
    # =====================================================
    with col2:

        st.markdown("""
        <div class="cart-box">
        <h1>🛒</h1>
        <h2>Pesanan</h2>
        </div>
        """, unsafe_allow_html=True)

        total = 0

        for item, harga in st.session_state.cart:
            st.write(f"🍽 {item}")
            st.write(f"💰 Rp{harga:,}")
            total += harga

        st.markdown("---")

        st.subheader(f"💵 Total : Rp{total:,}")

        nama = st.text_input("Nama Pemesan")

        bayar = st.selectbox(
            "Metode Pembayaran",
            ["QRIS", "Cash", "Transfer"]
        )

        if bayar == "QRIS":
            st.image(
                "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=GG-BITES-PAYMENT"
            )

        if st.button("✅ Checkout"):

            if len(st.session_state.cart) == 0:
                st.warning("Keranjang kosong!")

            else:

                pesanan = {
                    "nama": nama,
                    "items": st.session_state.cart,
                    "total": total,
                    "bayar": bayar,
                    "waktu": datetime.now().strftime("%H:%M:%S")
                }

                st.session_state.orders.append(pesanan)

                st.success("Pesanan berhasil dibuat 🍔")
                st.toast("Pesanan Baru Masuk 🔔")

                st.session_state.cart = []

# =========================================================
# COMBO
# =========================================================
elif menu == "🍟 Combo Recommendation":

    st.title("🍟 Combo Recommendation")

    cari = st.text_input("Cari menu")

    if cari:

        ditemukan = False

        for menu_combo, rekom in app.combo.items():

            if cari.lower() in menu_combo.lower():

                ditemukan = True

                st.subheader(f"🍔 {menu_combo}")

                cols = st.columns(len(rekom))

                for i, item in enumerate(rekom):

                    with cols[i]:

                        st.markdown(f"""
                        <div class="food-card">
                        <div class="food-emoji">
                        {app.emoji.get(item,"🍽")}
                        </div>

                        <div class="food-name">
                        {item}
                        </div>
                        </div>
                        """, unsafe_allow_html=True)

        if not ditemukan:
            st.error("Menu combo tidak ditemukan")

# =========================================================
# TOP MENU
# =========================================================
elif menu == "🍕 Top Menu":

    st.title("🍕 Top Menu")

    top = [
        ("Wagyu Steak", "🥩"),
        ("Pizza Supreme", "🍕"),
        ("Double Beef Burger", "🍔"),
        ("Premium Matcha Latte", "🍵")
    ]

    cols = st.columns(4)

    for i, (nama, emoji) in enumerate(top):

        with cols[i]:

            st.markdown(f"""
            <div class="food-card">
            <div class="food-emoji">{emoji}</div>

            <div class="food-name">
            {nama}
            </div>

            <div class="food-price">
            🔥 TOP MENU
            </div>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# RANDOM PICK
# =========================================================
elif menu == "🎲 Random Pick":

    semua = []

    for kategori, data in app.kategori.items():
        for nama_menu, daftar in data.items():
            for item in daftar:
                semua.append(item)

    pilih = random.choice(semua)

    st.markdown(f"""
    <div class="food-card">

    <div class="food-emoji">
    🎲
    </div>

    <div class="food-name">
    {pilih[0]}
    </div>

    <div class="food-price">
    Rp{pilih[1]:,}
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# HARGA
# =========================================================
elif menu == "💰 Rekomendasi Harga":

    pilihan = st.selectbox(
        "Pilih Kategori",
        ["Murah", "Sedang", "Mahal"]
    )

    semua = []

    for kategori, data in app.kategori.items():
        for nama_menu, daftar in data.items():
            semua.extend(daftar)

    hasil = []

    if pilihan == "Murah":
        hasil = [x for x in semua if x[1] <= 25000]

    elif pilihan == "Sedang":
        hasil = [x for x in semua if 25000 < x[1] <= 50000]

    else:
        hasil = [x for x in semua if x[1] > 50000]

    cols = st.columns(4)

    for i, (nama, harga) in enumerate(hasil):

        with cols[i % 4]:

            st.markdown(f"""
            <div class="food-card">

            <div class="food-emoji">
            🍽
            </div>

            <div class="food-name">
            {nama}
            </div>

            <div class="food-price">
            Rp{harga:,}
            </div>

            </div>
            """, unsafe_allow_html=True)

# =========================================================
# SEARCH
# =========================================================
elif menu == "🔍 Search Menu":

    st.title("🔍 Search Menu")

    keyword = st.text_input("Cari makanan")

    if keyword:

        ditemukan = False

        cols = st.columns(4)

        semua = []

        for kategori, data in app.kategori.items():
            for nama_menu, daftar in data.items():
                semua.extend(daftar)

        for i, (nama, harga) in enumerate(semua):

            if keyword.lower() in nama.lower():

                ditemukan = True

                with cols[i % 4]:

                    st.markdown(f"""
                    <div class="food-card">

                    <div class="food-emoji">
                    🍽
                    </div>

                    <div class="food-name">
                    {nama}
                    </div>

                    <div class="food-price">
                    Rp{harga:,}
                    </div>

                    </div>
                    """, unsafe_allow_html=True)

        if not ditemukan:
            st.error("Menu tidak ditemukan!")

# =========================================================
# ADMIN
# =========================================================
elif menu == "🔐 Admin":

    st.title("🔐 Admin Dashboard")

    kode = st.text_input(
        "Masukkan Kode Admin",
        type="password"
    )

    if kode == app.admin_code:

        st.success("Login berhasil ✅")

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
                    st.write(f"💳 Pembayaran : {order['bayar']}")

                    st.write("🍽 Menu :")

                    for item, harga in order["items"]:
                        st.write(f"- {item} | Rp{harga:,}")

                    st.success(f"💰 Total : Rp{order['total']:,}")

    elif kode != "":
        st.error("Kode admin salah ❌")
