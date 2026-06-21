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
    page_icon="🍱",
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

        self.kategori = {

            "🍱 Makanan Berat": {

                "Bakso": [
                ("Bakso Urat", 18000, 4),
                ("Bakso Jumbo", 25000, 5),
                ("Bakso Mercon", 22000, 4),
                ("Bakso Halus", 17000, 4)
            ],
            "Mie Ayam": [
                ("Mie Ayam Bakso", 20000, 4),
                ("Mie Ayam Ceker", 23000, 5),
                ("Mie Ayam Pangsit", 18000, 4),
                ("Mie Ayam Jumbo", 27000, 4)
            ],
            "Nasi Goreng": [
                ("Nasi Goreng Seafood", 35000, 5),
                ("Nasi Goreng Kampung", 18000, 4),
                ("Nasi Goreng Mawut", 25000, 4),
                ("Nasi Goreng Spesial", 30000, 5)
            ],
            "Ayam Geprek": [
                ("Ayam Geprek Mozarella", 35000, 5),
                ("Ayam Geprek Keju", 30000, 4),
                ("Ayam Geprek Sambal Matah", 28000, 5),
                ("Ayam Geprek Jumbo", 40000, 5)
            ],
            "Burger": [
                ("Cheese Burger", 25000, 4),
                ("Double Beef Burger", 45000, 5),
                ("Chicken Burger", 22000, 5),
                ("BBQ Burger", 35000, 4)
            ],
            "Pizza": [
                ("Pizza Pepperoni", 70000, 4),
                ("Pizza Mozarella", 80000, 5),
                ("Pizza Supreme", 95000, 5),
                ("Pizza Beef", 85000, 5)
            ],
            "Steak": [
                ("Chicken Steak", 50000, 5),
                ("Sirloin Steak", 85000, 4),
                ("Tenderloin Steak", 120000, 5),
                ("Wagyu Steak", 180000, 5)
            ],
            "Sate Ayam": [
                ("Sate Ayam Madura", 25000, 4),
                ("Sate Ayam Taichan", 30000, 5),
                ("Sate Ayam Jumbo", 35000, 5),
                ("Sate Ayam Pedas", 28000, 4)
            ],
            "Soto": [
                ("Soto Ayam", 20000, 5),
                ("Soto Lamongan", 25000, 4),
                ("Soto Betawi", 35000, 4),
                ("Soto Daging", 40000, 4)
            ]
            },

            "🍟 Makanan Ringan": {

                "Kentang Goreng": [
                ("French Fries BBQ", 18000, 4),
                ("French Fries Cheese", 25000, 4),
                ("French Fries Spicy", 20000, 5),
                ("Loaded Fries", 35000, 5)
            ],
            "Cilok": [
                ("Cilok Kuah", 12000, 4),
                ("Cilok Pedas", 15000, 5),
                ("Cilok Mozarella", 22000, 4),
                ("Cilok Isi Ayam", 18000, 5)
            ],
            "Batagor": [
                ("Batagor Kuah", 20000, 4),
                ("Batagor Kering", 18000, 5),
                ("Batagor Mozarella", 30000, 4),
                ("Batagor Spesial", 35000, 5)
            ],
            "Sosis Bakar": [
                ("Sosis Bakar Jumbo", 20000, 5),
                ("Sosis Bakar BBQ", 18000, 5),
                ("Sosis Bakar Keju", 25000, 4),
                ("Sosis Bakar Pedas", 22000, 4)
            ],
            "Roti Bakar": [
                ("Roti Bakar Coklat", 18000, 5),
                ("Roti Bakar Keju", 20000, 4),
                ("Roti Bakar Oreo", 25000, 4),
                ("Roti Bakar Tiramisu", 28000, 5)
            ],
            "Siomay": [
                ("Siomay Bandung", 22000, 5),
                ("Siomay Jumbo", 28000, 4),
                ("Siomay Pedas", 25000, 4),
                ("Siomay Seafood", 35000, 5)
            ],
            "Dimsum": [
                ("Dimsum Original", 18000, 4),
                ("Dimsum Chili Oil", 22000, 4),
                ("Dimsum Mentai", 30000, 5),
                ("Dimsum Mozarella", 28000, 4)
            ],
            "Corndog": [
                ("Corndog Mozarella", 25000, 5),
                ("Corndog Sosis", 22000, 4),
                ("Corndog Coklat", 28000, 5),
                ("Corndog Spicy Mayo", 30000, 4)
            ]
            },

            "🍰 Dessert": {

                "Donat": [
                ("Donat Coklat", 12000, 5),
                ("Donat Strawberry", 15000, 5),
                ("Donat Oreo", 18000, 4),
                ("Donat Tiramisu", 22000, 5)
            ],
            "Brownies": [
                ("Brownies Kukus", 25000, 4),
                ("Brownies Lumer", 30000, 5),
                ("Brownies Almond", 35000, 5),
                ("Brownies Keju", 32000, 5)
            ],
            "Es Krim": [
                ("Es Krim Vanilla", 15000, 5),
                ("Es Krim Coklat", 18000, 5),
                ("Es Krim Strawberry", 20000, 5),
                ("Es Krim Matcha", 28000, 5)
            ],
            "Cheesecake": [
                ("Cheesecake Oreo", 40000, 4),
                ("Cheesecake Matcha", 50000, 4),
                ("Cheesecake Strawberry", 45000, 5),
                ("Cheesecake Blueberry", 55000, 5)
            ],
            "Waffle": [
                ("Waffle Coklat", 25000, 5),
                ("Waffle Strawberry", 28000, 4),
                ("Waffle Ice Cream", 35000, 5),
                ("Waffle Matcha", 40000, 4)
            ],
            "Pancake": [
                ("Pancake Maple", 25000, 5),
                ("Pancake Coklat", 28000, 5),
                ("Pancake Strawberry", 30000, 4),
                ("Pancake Ice Cream", 38000, 5)
            ],
            "Coklat Dubai": [
                ("Coklat Dubai Mini", 50000, 4),
                ("Coklat Dubai", 250000, 5),
                ("Dubai Chewy Cookie Mini", 25000, 5),
                ("Dubai Chewy Cookie Jumbo", 150000, 5)
            ]
            },

            "🥤 Minuman": {

                "Thai Tea": [
                ("Thai Tea Original", 15000, 4),
                ("Thai Tea Cheese", 25000, 5),
                ("Thai Tea Brown Sugar", 30000, 4),
                ("Thai Tea Jumbo", 22000, 5)
            ],
            "Boba Brown Sugar": [
                ("Brown Sugar Fresh Milk", 30000, 5),
                ("Brown Sugar Regal", 35000, 4),
                ("Brown Sugar Oreo", 40000, 4),
                ("Brown Sugar Cheese", 45000, 4)
            ],
            "Kopi Latte": [
                ("Vanilla Latte", 30000, 5),
                ("Hazelnut Latte", 35000, 4),
                ("Caramel Latte", 38000, 5),
                ("Mocha Latte", 42000, 4)
            ],
            "Milkshake": [
                ("Chocolate Milkshake", 25000, 4),
                ("Vanilla Milkshake", 28000, 5),
                ("Strawberry Milkshake", 30000, 5),
                ("Oreo Milkshake", 35000, 4)
            ],
            "Es Jeruk": [
                ("Es Jeruk Peras", 12000, 4),
                ("Orange Float", 25000, 5),
                ("Es Jeruk Jumbo", 18000, 5),
                ("Es Jeruk Nipis", 15000, 4)
            ],
            "Lemon Tea": [
                ("Lemon Tea Original", 15000, 5),
                ("Honey Lemon Tea", 25000, 5),
                ("Lychee Lemon Tea", 30000, 4),
                ("Yakult Lemon Tea", 35000, 4)
            ],
            "Matcha Latte": [
                ("Matcha Latte Original", 35000, 4),
                ("Creamy Matcha Latte", 45000, 4),
                ("Premium Matcha Latte", 65000, 5),
                ("Matcha Brown Sugar", 50000, 4)
            ],
            "Yakult": [
                ("Yakult Strawberry", 25000, 4),
                ("Yakult Mango", 28000, 5),
                ("Yakult Lychee", 30000, 5),
                ("Yakult Mix Berry", 35000, 4)
            ]
            }
        }


        self.graph_combo = {

            "Bakso": [
                ("Es Jeruk Peras", 20000, 5),
                ("Cilok", 15000, 4)
            ],

            "Burger": [
                ("Milkshake", 30000, 5),
                ("Kentang Goreng", 18000, 5)
            ],

            "Pizza": [
                ("Thai Tea", 25000, 5),
                ("Kentang Goreng", 18000, 4)
            ],

            "Steak": [
                ("Matcha Latte", 35000, 5),
                ("Brownies", 30000, 5)
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
    background:linear-gradient(
        135deg,
        #fff5f5,
        #fff9e6,
        #eef8ff
    );
}

.header{
    text-align:center;
    padding:20px;
}

.title{
    font-size:60px;
    font-weight:900;
}

.title-text{
    background:linear-gradient(
        90deg,
        #ff512f,
        #dd2476,
        #ffb347
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    font-size:22px;
    color:#666;
}
@keyframes floating {

    0%{
        transform:translateY(0px);
    }

    50%{
        transform:translateY(-10px);
    }

    100%{
        transform:translateY(0px);
    }

}

.food-card{
    background:linear-gradient(
        145deg,
        #ffffff,
        #fff5f8,
        #fffdf6
    );

    border-radius:25px;
    padding:20px;
    text-align:center;
    margin-bottom:20px;
    height:320px;

    border:none;

    box-shadow:
        0 15px 30px rgba(0,0,0,.08),
        0 5px 15px rgba(255,79,139,.15);

    transition:.3s;
}

.food-card:hover{
    transform:translateY(-15px) scale(1.05);

    box-shadow:
        0 25px 40px rgba(0,0,0,.20),
        0 12px 25px rgba(255,81,47,.35);
}


.food-emoji{
    font-size:60px;
}

.food-name{
    font-size:22px;
    font-weight:700;
    margin-top:10px;
    color:#333;
}

.food-price{
    color:#ff4f8b;
    font-size:26px;
    font-weight:bold;
    margin-top:10px;
    text-shadow:0 0 8px rgba(255,79,139,0.25);
}

.category-title{
    font-size:30px;
    font-weight:bold;

    background:linear-gradient(
        135deg,
        #ff512f,
        #f09819
    );

    color:white;

    padding:15px 25px;
    border-radius:15px;

    margin-top:30px;
    margin-bottom:15px;

    box-shadow:
        0 8px 20px rgba(255,81,47,.25);
}

.sub-menu{
    font-size:22px;
    font-weight:bold;

    background:linear-gradient(
        135deg,
        #667eea,
        #764ba2
    );

    color:white;

    padding:10px 20px;
    border-radius:12px;

    display:inline-block;

    margin-top:20px;
    margin-bottom:15px;
}

.stButton>button{
    width:100%;
    border:none;
    border-radius:15px;
    height:50px;

    background:linear-gradient(
        135deg,
        #ff512f,
        #dd2476
    );

    color:white;
    font-weight:bold;

    box-shadow:
        0 8px 20px rgba(221,36,118,.35);
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
    <div class="title">
    <span>🍱</span>
    <span class="title-text">GG BITES</span>
    <span>🍱</span>
    </div>
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
        "🍱 Order Menu",
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

            st.success("Pesanan berhasil dibuat 🍱")

            st.session_state.cart = []

    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"
        st.rerun()

# =========================================================
# ORDER MENU
# =========================================================
else:

    if menu == "🍱 Order Menu":

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

                for i, (nama, harga, rating) in enumerate(daftar):

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

                        <div>
                        {"⭐" * rating}
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

            for menu_combo, rekom in app.graph_combo.items():

                if cari.lower() in menu_combo.lower():

                    ditemukan = True

                    st.subheader(menu_combo)

                    cols = st.columns(len(rekom))

                    for i, (nama, harga, rating) in enumerate(rekom):

                        with cols[i]:

                            st.markdown(f"""
                            <div class="food-card">
                            <div class="food-emoji">
                            {app.emoji.get(nama,'🍊')}
                            </div>
                            <div class="food-name">
                            {nama}
                            </div>
                            <div class="food-price">
                            Rp{harga:,}
                            </div>
                            <div>
                             {"⭐"* rating}
                            </div>
                            </div>
                            """, unsafe_allow_html=True)

            if not ditemukan:
                st.error("Combo tidak ditemukan")

    elif menu == "🍕 Top Menu":

        st.title("🍕 Top Menu")

        top = [
            ("🍔", "Double Beef Burger",5),
            ("🍕", "Pizza Supreme",5),
            ("🥩", "Wagyu Steak",5),
            ("🍵", "Premium Matcha Latte",5)
        ]

        cols = st.columns(4)

        for i, (emoji, nama,rating) in enumerate(top):

            with cols[i]:

                st.markdown(f"""
                <div class="food-card">
                <div class="food-emoji">{emoji}</div>
                <div class="food-name">{nama}</div>
                <div class="food-price">BEST SELLER</div>
                <div>{"⭐" * rating}</div>
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
        <div>
        {"⭐" * pick[2]}
        </div>
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

        for i, (nama, harga, rating) in enumerate(hasil):

            with cols[i % 4]:

                st.markdown(f"""
                <div class="food-card">
                <div class="food-emoji">💰</div>
                <div class="food-name">{nama}</div>
                <div class="food-price">Rp{harga:,}</div>
                <div>
                {"⭐" * rating}
                </div>
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

            for i, (nama, harga, rating) in enumerate(semua):

                if keyword.lower() in nama.lower():

                    ditemukan = True

                    with cols[i % 4]:

                        st.markdown(f"""
                        <div class="food-card">
                        <div class="food-emoji">🔍</div>
                        <div class="food-name">{nama}</div>
                        <div class="food-price">Rp{harga:,}</div>
                        <div>
                        {"⭐" * rating}
                        </div>
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
