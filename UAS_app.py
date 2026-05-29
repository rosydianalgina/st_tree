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

        self.menu = {

            "🍜 Bakso": 25000,
            "🍔 Burger": 35000,
            "🍕 Pizza": 85000,
            "🍟 Kentang Goreng": 20000,
            "🍩 Donat": 18000,
            "🧋 Boba Brown Sugar": 30000,
            "🍗 Ayam Geprek": 32000,
            "🍣 Sushi": 40000,
            "🥩 Steak": 120000,
            "🍵 Matcha Latte": 35000,
            "🥛 Milkshake": 28000,
            "🍚 Nasi Goreng": 25000

        }

        # =================================================
        # GRAPH REKOMENDASI
        # =================================================
        self.graph_rekomendasi = {

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

            "Donat": [
                ("Matcha Latte", 5),
                ("Milkshake", 4)
            ]
        }

app = GGBitesGraph()

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

.stApp{
    background-color:#f7f3ef;
}

/* HEADER */

.title{
    font-size:60px;
    font-weight:bold;
    color:#ff4f8b;
}

.subtitle{
    color:gray;
    margin-bottom:20px;
}

/* MENU CARD */

.card{
    background:white;
    border-radius:25px;
    padding:20px;
    text-align:center;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
    transition:0.3s;
}

.card:hover{
    transform:scale(1.03);
}

.food-emoji{
    font-size:55px;
}

.food-name{
    font-size:22px;
    font-weight:bold;
    margin-top:10px;
}

.food-price{
    color:#ff4f8b;
    font-size:22px;
    font-weight:bold;
    margin-top:10px;
}

/* CART */

.cart-box{
    background:white;
    padding:20px;
    border-radius:25px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    position:sticky;
    top:20px;
}

/* BUTTON */

.stButton > button{
    width:100%;
    background:linear-gradient(90deg,#ff7aa8,#ff4f8b);
    color:white;
    border:none;
    border-radius:15px;
    font-weight:bold;
    padding:10px;
}

.stButton > button:hover{
    background:linear-gradient(90deg,#ff4f8b,#ff7aa8);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class='title'>
💖 GG BITES
</div>

<div class='subtitle'>
McD Style Food Ordering System
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
menu_sidebar = st.sidebar.radio(

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
if menu_sidebar == "🍔 Order Menu":

    col1, col2 = st.columns([3,1])

    # =====================================================
    # MENU MAKANAN
    # =====================================================
    with col1:

        st.subheader("🍽️ Pilih Menu")

        cols = st.columns(3)

        nomor = 0

        for nama, harga in app.menu.items():

            with cols[nomor % 3]:

                emoji = nama.split()[0]
                nama_makanan = " ".join(nama.split()[1:])

                st.markdown(f"""
                <div class='card'>
                    <div class='food-emoji'>
                        {emoji}
                    </div>

                    <div class='food-name'>
                        {nama_makanan}
                    </div>

                    <div class='food-price'>
                        Rp{harga:,}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(
                    f"Tambah {nama_makanan}",
                    key=nama
                ):

                    st.session_state.cart.append(
                        (nama_makanan, harga)
                    )

                    st.success(
                        f"{nama_makanan} masuk cart!"
                    )

            nomor += 1

    # =====================================================
    # CART
    # =====================================================
    with col2:

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

            st.subheader(f"Total : Rp{total:,}")

            nama = st.text_input(
                "Nama Pemesan"
            )

            pembayaran = st.selectbox(

                "Pembayaran",

                [
                    "QRIS",
                    "Cash",
                    "DANA",
                    "OVO",
                    "GoPay"
                ]
            )

            if st.button("Checkout"):

                data = {

                    "nama": nama,
                    "pesanan": st.session_state.cart,
                    "total": total,
                    "pembayaran": pembayaran,
                    "waktu": datetime.now().strftime("%d/%m/%Y %H:%M")
                }

                st.session_state.orders.append(data)

                st.success(
                    "✅ Pesanan berhasil!"
                )

                st.balloons()

                st.session_state.cart = []

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SEARCH REKOMENDASI
# =========================================================
elif menu_sidebar == "🔍 Cari Rekomendasi":

    st.subheader("🔍 Cari Rekomendasi")

    cari = st.text_input(
        "Cari makanan..."
    )

    if cari:

        ditemukan = False

        for makanan, rekomendasi in app.graph_rekomendasi.items():

            if cari.lower() in makanan.lower():

                ditemukan = True

                st.markdown(f"""
                ## 🍽️ {makanan}
                """)

                cols = st.columns(2)

                for i, (menu, rating) in enumerate(rekomendasi):

                    with cols[i % 2]:

                        st.markdown(f"""
                        <div class='card'>
                        <h2>{menu}</h2>
                        <h3>{"⭐" * rating}</h3>
                        </div>
                        """, unsafe_allow_html=True)

        if not ditemukan:

            st.error("❌ Menu tidak ditemukan")

# =========================================================
# TOP RATING
# =========================================================
elif menu_sidebar == "⭐ Top Rating":

    st.subheader("⭐ Top Rating")

    top = [

        "Wagyu Steak",
        "Pizza Supreme",
        "Double Beef Burger",
        "Matcha Latte"
    ]

    cols = st.columns(4)

    for i, item in enumerate(top):

        with cols[i]:

            st.markdown(f"""
            <div class='card'>
            <h2>{item}</h2>
            <h3>⭐⭐⭐⭐⭐</h3>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# COMBO
# =========================================================
elif menu_sidebar == "💡 Combo Recommendation":

    st.subheader("💡 Combo Recommendation")

    for makanan, combo in app.graph_rekomendasi.items():

        st.markdown(f"""
        <div class='card'>
        <h2>🍽️ {makanan}</h2>
        """, unsafe_allow_html=True)

        for item, rating in combo:

            st.write(
                f"✨ {item} {'⭐' * rating}"
            )

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RANDOM PICK
# =========================================================
elif menu_sidebar == "🎲 Random Pick":

    st.subheader("🎲 Random Pick")

    pilihan = random.choice(
        list(app.menu.items())
    )

    st.markdown(f"""
    <div class='card'>
        <div class='food-emoji'>
            🎲
        </div>

        <div class='food-name'>
            {pilihan[0]}
        </div>

        <div class='food-price'>
            Rp{pilihan[1]:,}
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# REKOMENDASI HARGA
# =========================================================
elif menu_sidebar == "💰 Rekomendasi Harga":

    st.subheader("💰 Rekomendasi Harga")

    kategori = st.radio(

        "Pilih Kategori",

        [
            "Murah",
            "Sedang",
            "Mahal"
        ]
    )

    hasil = []

    for nama, harga in app.menu.items():

        if kategori == "Murah" and harga <= 25000:
            hasil.append((nama, harga))

        elif kategori == "Sedang" and 25000 < harga <= 50000:
            hasil.append((nama, harga))

        elif kategori == "Mahal" and harga > 50000:
            hasil.append((nama, harga))

    cols = st.columns(3)

    for i, (nama, harga) in enumerate(hasil):

        with cols[i % 3]:

            st.markdown(f"""
            <div class='card'>
            <h2>{nama}</h2>
            <h3>Rp{harga:,}</h3>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# ADMIN
# =========================================================
elif menu_sidebar == "🔐 Admin":

    st.subheader("🔐 Admin Dashboard")

    kode = st.text_input(

        "Masukkan Kode Admin",
        type="password"
    )

    # KODE ADMIN
    # GGBITES123

    if kode == "GGBITES123":

        st.success("✅ Login berhasil")

        if len(st.session_state.orders) == 0:

            st.info("Belum ada pesanan")

        else:

            for i, order in enumerate(
                st.session_state.orders,
                start=1
            ):

                st.markdown(f"""
                <div class='card'>
                <h2>📦 Order #{i}</h2>

                👤 {order['nama']} <br>
                💳 {order['pembayaran']} <br>
                💰 Rp{order['total']:,} <br>
                🕒 {order['waktu']}
                </div>
                """, unsafe_allow_html=True)

                st.write("### Detail Pesanan")

                for item, harga in order["pesanan"]:

                    st.write(
                        f"🍽️ {item} - Rp{harga:,}"
                    )

    else:

        st.warning(
            "Masukkan kode admin"
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
