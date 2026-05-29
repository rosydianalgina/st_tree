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

        # =================================================
        # EMOJI
        # =================================================
        self.emoji = {

            "Bakso": "🍜",
            "Mie Ayam": "🍜",
            "Nasi Goreng": "🍚",
            "Ayam Geprek": "🍗",
            "Burger": "🍔",
            "Pizza": "🍕",
            "Steak": "🥩",

            "Kentang Goreng": "🍟",
            "Cilok": "🍡",
            "Batagor": "🥟",

            "Donat": "🍩",
            "Brownies": "🧁",
            "Es Krim": "🍦",

            "Thai Tea": "🥤",
            "Boba Brown Sugar": "🧋",
            "Matcha Latte": "🍵"
        }

        # =================================================
        # KATEGORI
        # =================================================
        self.kategori = {

            "🍽️ Makanan Berat": {

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

                "Matcha Latte": [
                    ("Matcha Latte Original", 35000),
                    ("Creamy Matcha Latte", 45000),
                    ("Premium Matcha Latte", 65000),
                    ("Matcha Brown Sugar", 50000)
                ]
            }
        }

        # =================================================
        # COMBO
        # =================================================
        self.graph_combo = {

            "Burger": [
                ("Milkshake", 5),
                ("Kentang Goreng", 5)
            ],

            "Pizza": [
                ("Lemon Tea", 4),
                ("Kentang Goreng", 5)
            ],

            "Bakso": [
                ("Es Jeruk", 5),
                ("Kentang Goreng", 4)
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
    background:linear-gradient(
        to bottom right,
        #f8f5f1,
        #fffaf7
    );
}

/* HEADER */

.main-header{
    text-align:center;
    margin-bottom:40px;
}

.title{
    font-size:70px;
    font-weight:900;
    color:#ff5b93;
}

.subtitle{
    font-size:22px;
    color:#666;
    margin-top:-10px;
}

/* CATEGORY */

.category-title{
    font-size:35px;
    font-weight:bold;
    color:#333;
    margin-top:40px;
    margin-bottom:20px;
}

/* SUB MENU */

.sub-menu{
    font-size:24px;
    font-weight:bold;
    color:#555;
    margin-top:20px;
    margin-bottom:15px;
}

/* CARD */

.card{

    background:white;

    border-radius:25px;

    padding:20px;

    height:280px;

    display:flex;

    flex-direction:column;

    justify-content:space-between;

    align-items:center;

    text-align:center;

    box-shadow:0 4px 15px rgba(0,0,0,0.08);

    margin-bottom:20px;

    transition:0.3s;
}

.card:hover{

    transform:translateY(-5px);

    box-shadow:0 8px 20px rgba(0,0,0,0.12);
}

/* EMOJI */

.food-emoji{
    font-size:60px;
}

/* NAME */

.food-name{
    font-size:20px;
    font-weight:bold;
    color:#333;
}

/* PRICE */

.food-price{
    font-size:24px;
    font-weight:bold;
    color:#ff5b93;
}

/* BUTTON */

.stButton > button{

    width:100%;

    border:none;

    border-radius:15px;

    padding:12px;

    background:linear-gradient(
        90deg,
        #ff8ab3,
        #ff5b93
    );

    color:white;

    font-size:16px;

    font-weight:bold;
}

.stButton > button:hover{

    background:linear-gradient(
        90deg,
        #ff5b93,
        #ff8ab3
    );
}

/* CART */

.cart-box{

    background:white;

    border-radius:25px;

    padding:25px;

    box-shadow:0 4px 15px rgba(0,0,0,0.08);

    position:sticky;

    top:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class='main-header'>

<div class='title'>
💖 GG BITES 💖
</div>

<div class='subtitle'>
McD Style Food Ordering System
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
        "🔍 Cari Rekomendasi",
        "⭐ Top Rating",
        "💡 Combo Recommendation",
        "🎲 Random Pick",
        "💰 Rekomendasi Harga",
        "🔐 Admin"
    ]
)

# =========================================================
# ORDER MENU
# =========================================================
if menu == "🍔 Order Menu":

    kiri, kanan = st.columns([3,1])

    # =====================================================
    # MENU
    # =====================================================
    with kiri:

        for kategori, isi in app.kategori.items():

            st.markdown(f"""
            <div class='category-title'>
            {kategori}
            </div>
            """, unsafe_allow_html=True)

            for jenis_menu, daftar_menu in isi.items():

                st.markdown(f"""
                <div class='sub-menu'>
                {app.emoji.get(jenis_menu,'🍽️')} {jenis_menu}
                </div>
                """, unsafe_allow_html=True)

                cols = st.columns(4)

                for i, (nama, harga) in enumerate(daftar_menu):

                    with cols[i % 4]:

                        st.markdown(f"""
                        <div class='card'>

                            <div class='food-emoji'>
                            {app.emoji.get(jenis_menu,'🍽️')}
                            </div>

                            <div class='food-name'>
                            {nama}
                            </div>

                            <div class='food-price'>
                            Rp{harga:,}
                            </div>

                        </div>
                        """, unsafe_allow_html=True)

                        if st.button(
                            "🛒 Tambah",
                            key=nama
                        ):

                            st.session_state.cart.append(
                                (nama, harga)
                            )

                            st.success(
                                f"{nama} ditambahkan!"
                            )

    # =====================================================
    # CART
    # =====================================================
    with kanan:

        st.markdown("""
        <div class='cart-box'>
        <h2>🛒 Pesanan</h2>
        """, unsafe_allow_html=True)

        total = 0

        if len(st.session_state.cart) == 0:

            st.info("Belum ada pesanan")

        else:

            for item, harga in st.session_state.cart:

                st.write(f"🍽️ {item}")
                st.write(f"💰 Rp{harga:,}")

                total += harga

                st.divider()

            st.subheader(
                f"💰 Total : Rp{total:,}"
            )

            nama = st.text_input(
                "Nama Pemesan"
            )

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

            # QRIS
            if pembayaran == "QRIS":

                st.image(
                    "https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=GGBITESPAYMENT"
                )

                st.success(
                    "Silahkan scan QRIS"
                )

            if st.button("✅ Checkout"):

                data = {

                    "nama": nama,
                    "pesanan": st.session_state.cart,
                    "total": total,
                    "pembayaran": pembayaran,
                    "waktu": datetime.now().strftime("%d/%m/%Y %H:%M")
                }

                st.session_state.orders.append(data)

                st.success(
                    "Pesanan berhasil dibuat!"
                )

                st.balloons()

                st.session_state.cart = []

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SEARCH MENU
# =========================================================
elif menu == "🔍 Cari Rekomendasi":

    st.subheader("🔍 Cari Rekomendasi")

    cari = st.text_input(
        "Cari menu..."
    )

    if cari:

        ditemukan = False

        for kategori, isi in app.kategori.items():

            for jenis, daftar in isi.items():

                if cari.lower() in jenis.lower():

                    ditemukan = True

                    st.markdown(f"## {jenis}")

                    cols = st.columns(4)

                    for i, (nama, harga) in enumerate(daftar):

                        with cols[i % 4]:

                            st.markdown(f"""
                            <div class='card'>

                            <div class='food-emoji'>
                            🔍
                            </div>

                            <div class='food-name'>
                            {nama}
                            </div>

                            <div class='food-price'>
                            Rp{harga:,}
                            </div>

                            </div>
                            """, unsafe_allow_html=True)

        if not ditemukan:

            st.error("❌ Menu tidak ditemukan")

# =========================================================
# TOP RATING
# =========================================================
elif menu == "⭐ Top Rating":

    top = [

        ("Wagyu Steak", "⭐⭐⭐⭐⭐"),
        ("Pizza Supreme", "⭐⭐⭐⭐⭐"),
        ("Double Beef Burger", "⭐⭐⭐⭐⭐"),
        ("Premium Matcha Latte", "⭐⭐⭐⭐⭐")
    ]

    cols = st.columns(4)

    for i, (nama, rating) in enumerate(top):

        with cols[i]:

            st.markdown(f"""
            <div class='card'>

            <div class='food-emoji'>
            🏆
            </div>

            <div class='food-name'>
            {nama}
            </div>

            <div class='food-price'>
            {rating}
            </div>

            </div>
            """, unsafe_allow_html=True)

# =========================================================
# COMBO RECOMMENDATION
# =========================================================
elif menu == "💡 Combo Recommendation":

    st.subheader("💡 Combo Recommendation")

    cari_combo = st.text_input(
        "Cari combo..."
    )

    if cari_combo:

        ditemukan = False

        for makanan, combo in app.graph_combo.items():

            if cari_combo.lower() in makanan.lower():

                ditemukan = True

                st.markdown(f"## 🍽️ {makanan}")

                cols = st.columns(2)

                for i, (item, rating) in enumerate(combo):

                    with cols[i % 2]:

                        st.markdown(f"""
                        <div class='card'>

                        <div class='food-emoji'>
                        ✨
                        </div>

                        <div class='food-name'>
                        {item}
                        </div>

                        <div class='food-price'>
                        {'⭐' * rating}
                        </div>

                        </div>
                        """, unsafe_allow_html=True)

        if not ditemukan:

            st.error("❌ Combo tidak ditemukan")

# =========================================================
# RANDOM PICK
# =========================================================
elif menu == "🎲 Random Pick":

    semua = []

    for kategori, isi in app.kategori.items():

        for jenis, daftar in isi.items():

            semua.extend(daftar)

    pick = random.choice(semua)

    st.markdown(f"""
    <div class='card'>

    <div class='food-emoji'>
    🎲
    </div>

    <div class='food-name'>
    {pick[0]}
    </div>

    <div class='food-price'>
    Rp{pick[1]:,}
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# REKOMENDASI HARGA
# =========================================================
elif menu == "💰 Rekomendasi Harga":

    pilihan = st.radio(

        "Pilih Harga",

        [
            "Murah",
            "Sedang",
            "Mahal"
        ]
    )

    semua = []

    for kategori, isi in app.kategori.items():

        for jenis, daftar in isi.items():

            semua.extend(daftar)

    if pilihan == "Murah":

        hasil = [
            x for x in semua
            if x[1] <= 25000
        ]

    elif pilihan == "Sedang":

        hasil = [
            x for x in semua
            if 25000 < x[1] <= 50000
        ]

    else:

        hasil = [
            x for x in semua
            if x[1] > 50000
        ]

    cols = st.columns(4)

    for i, (nama, harga) in enumerate(hasil):

        with cols[i % 4]:

            st.markdown(f"""
            <div class='card'>

            <div class='food-emoji'>
            💰
            </div>

            <div class='food-name'>
            {nama}
            </div>

            <div class='food-price'>
            Rp{harga:,}
            </div>

            </div>
            """, unsafe_allow_html=True)

# =========================================================
# ADMIN
# =========================================================
elif menu == "🔐 Admin":

    st.subheader("🔐 Admin Dashboard")

    kode = st.text_input(
        "Masukkan kode admin",
        type="password"
    )

    # KODE ADMIN
    # GGBITES123

    if kode == "GGBITES123":

        st.success("Login berhasil!")

        if len(st.session_state.orders) == 0:

            st.info("Belum ada pesanan")

        else:

            for i, order in enumerate(
                st.session_state.orders,
                start=1
            ):

                st.markdown(f"""
                <div class='card'>

                <div class='food-emoji'>
                📦
                </div>

                <div class='food-name'>
                Order #{i}
                </div>

                <div>
                👤 {order['nama']}<br>
                💳 {order['pembayaran']}<br>
                💰 Rp{order['total']:,}<br>
                🕒 {order['waktu']}
                </div>

                </div>
                """, unsafe_allow_html=True)

                st.write("### Detail Pesanan")

                for item, harga in order["pesanan"]:

                    st.write(
                        f"🍽️ {item} - Rp{harga:,}"
                    )
