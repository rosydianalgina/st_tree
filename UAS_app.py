import streamlit as st
import random

# =========================================================
# CONFIG STREAMLIT
# =========================================================
st.set_page_config(
    page_title="GG BITES",
    page_icon="🍽️",
    layout="wide"
)

# =========================================================
# CLASS GG BITES
# =========================================================
class GGBitesGraph:
    def __init__(self):

        # =================================================
        # EMOJI MENU
        # =================================================
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

        # =================================================
        # GRAPH REKOMENDASI
        # =================================================
        self.graph_rekomendasi = {
            "Bakso": [
                ("Bakso Urat", 18000),
                ("Bakso Jumbo", 25000),
                ("Bakso Mercon", 22000),
                ("Bakso Halus", 17000)
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

            "Thai Tea": [
                ("Thai Tea Original", 15000),
                ("Thai Tea Cheese", 25000),
                ("Thai Tea Brown Sugar", 30000),
                ("Thai Tea Jumbo", 22000)
            ],

            "Kopi Latte": [
                ("Vanilla Latte", 30000),
                ("Hazelnut Latte", 35000),
                ("Caramel Latte", 38000),
                ("Mocha Latte", 42000)
            ],

            "Coklat Dubai": [
                ("Coklat Dubai Mini", 50000),
                ("Coklat Dubai", 250000),
                ("Dubai Chewy Cookie Mini", 25000),
                ("Dubai Chewy Cookie Jumbo", 150000)
            ]
        }

        # =================================================
        # COMBO
        # =================================================
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
            ]
        }

    # =====================================================
    # FUNGSI BINTANG
    # =====================================================
    def bintang(self, rating):
        return "⭐" * rating


# =========================================================
# OBJECT
# =========================================================
app = GGBitesGraph()

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <h1 style='text-align:center;color:#ff4b4b;'>
    🍽️ GG BITES 🍽️
    </h1>
    <h4 style='text-align:center;'>
    Smart Food Recommendation System
    </h4>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR MENU
# =========================================================
menu = st.sidebar.selectbox(
    "📋 Pilih Menu",
    [
        "Lihat Menu",
        "Cari Rekomendasi",
        "Favorit Hari Ini",
        "Top Rating",
        "Combo Recommendation",
        "Random Pick",
        "Search Menu",
        "Rekomendasi Berdasarkan Harga"
    ]
)

# =========================================================
# MENU 1 - LIHAT MENU
# =========================================================
if menu == "Lihat Menu":

    st.subheader("📖 Daftar Menu")

    for kategori, daftar_menu in app.kategori.items():

        st.markdown(f"## 🍽️ {kategori}")

        cols = st.columns(3)

        for i, item in enumerate(daftar_menu):

            emoji = app.emoji.get(item, "🍽️")

            cols[i % 3].success(f"{emoji} {item}")

# =========================================================
# MENU 2 - CARI REKOMENDASI
# =========================================================
elif menu == "Cari Rekomendasi":

    st.subheader("🔍 Cari Rekomendasi")

    kategori = st.selectbox(
        "Pilih Kategori",
        list(app.kategori.keys())
    )

    menu_pilih = st.selectbox(
        "Pilih Menu",
        app.kategori[kategori]
    )

    if st.button("Tampilkan Rekomendasi"):

        hasil = app.graph_rekomendasi.get(menu_pilih, [])

        st.markdown(f"## ✨ Rekomendasi {menu_pilih}")

        for nama, harga in hasil:

            st.info(f"""
🍽️ {nama}

💰 Harga : Rp{harga:,}
""")

# =========================================================
# MENU 3 - FAVORIT HARI INI
# =========================================================
elif menu == "Favorit Hari Ini":

    st.subheader("🔥 Favorit Hari Ini")

    semua_menu = []

    for daftar in app.graph_rekomendasi.values():
        semua_menu.extend(daftar)

    pilihan = random.sample(semua_menu, min(5, len(semua_menu)))

    for nama, harga in pilihan:

        st.success(f"""
🍽️ {nama}

💰 Harga : Rp{harga:,}
""")

# =========================================================
# MENU 4 - TOP RATING
# =========================================================
elif menu == "Top Rating":

    st.subheader("🏆 Top Rating")

    top_menu = [
        ("Wagyu Steak", 5),
        ("Pizza Supreme", 5),
        ("Double Beef Burger", 5),
        ("Premium Matcha Latte", 5),
        ("Cheesecake Blueberry", 5)
    ]

    for nama, rating in top_menu:

        st.warning(f"""
🍽️ {nama}

⭐ Rating : {app.bintang(rating)}
""")

# =========================================================
# MENU 5 - COMBO
# =========================================================
elif menu == "Combo Recommendation":

    st.subheader("💡 Combo Recommendation")

    menu_combo = st.selectbox(
        "Pilih Menu",
        list(app.graph_combo.keys())
    )

    if st.button("Tampilkan Combo"):

        hasil = app.graph_combo[menu_combo]

        st.markdown(f"## 🍽️ {menu_combo} cocok dengan")

        for nama, skor in hasil:

            emoji = app.emoji.get(nama, "🍽️")

            st.info(f"""
{emoji} {nama}

⭐ Kecocokan : {app.bintang(skor)}
""")

# =========================================================
# MENU 6 - RANDOM PICK
# =========================================================
elif menu == "Random Pick":

    st.subheader("🎲 Random Pick")

    semua_menu = []

    for daftar in app.graph_rekomendasi.values():
        semua_menu.extend(daftar)

    pilihan = random.choice(semua_menu)

    st.success(f"""
🍽️ {pilihan[0]}

💰 Harga : Rp{pilihan[1]:,}
""")

# =========================================================
# MENU 7 - SEARCH MENU
# =========================================================
elif menu == "Search Menu":

    st.subheader("🔎 Search Menu")

    keyword = st.text_input("Cari menu")

    if keyword:

        ditemukan = False

        for daftar in app.graph_rekomendasi.values():

            for nama, harga in daftar:

                if keyword.lower() in nama.lower():

                    ditemukan = True

                    st.info(f"""
🍽️ {nama}

💰 Harga : Rp{harga:,}
""")

        if not ditemukan:
            st.error("❌ Menu tidak ditemukan!")

# =========================================================
# MENU 8 - REKOMENDASI BERDASARKAN HARGA
# =========================================================
elif menu == "Rekomendasi Berdasarkan Harga":

    st.subheader("💰 Rekomendasi Berdasarkan Harga")

    pilihan = st.radio(
        "Pilih Kategori Harga",
        ["Murah", "Sedang", "Mahal"]
    )

    semua = []

    for daftar in app.graph_rekomendasi.values():
        semua.extend(daftar)

    if pilihan == "Murah":

        hasil = [x for x in semua if x[1] <= 25000]

    elif pilihan == "Sedang":

        hasil = [x for x in semua if 25000 < x[1] <= 50000]

    else:

        hasil = [x for x in semua if x[1] > 50000]

    for nama, harga in hasil:

        st.success(f"""
🍽️ {nama}

💰 Harga : Rp{harga:,}
""")

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.caption("🍽️ GG BITES © 2026 | Streamlit App")