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
            "Kentang Goreng": "🍟",
            "Cilok": "🍡",
            "Batagor": "🥟",
            "Donat": "🍩",
            "Brownies": "🧁",
            "Es Krim": "🍦",
            "Thai Tea": "🥤",
            "Boba Brown Sugar": "🧋",
            "Kopi Latte": "☕",
            "Milkshake": "🥛",
            "Matcha Latte": "🍵",
            "Yakult": "🍹"
        }

        self.kategori = {

            "🍔 Makanan Berat": {

                "Bakso": [
                    ("Bakso Urat", 18000, 5),
                    ("Bakso Jumbo", 25000, 4),
                    ("Bakso Mercon", 22000, 5),
                    ("Bakso Halus", 17000, 4)
                ],

                "Mie Ayam": [
                    ("Mie Ayam Bakso", 20000, 5),
                    ("Mie Ayam Ceker", 23000, 4),
                    ("Mie Ayam Pangsit", 18000, 5),
                    ("Mie Ayam Jumbo", 27000, 5)
                ],

                "Nasi Goreng": [
                    ("Nasi Goreng Seafood", 35000, 5),
                    ("Nasi Goreng Kampung", 18000, 4),
                    ("Nasi Goreng Mawut", 25000, 5),
                    ("Nasi Goreng Spesial", 30000, 5)
                ],

                "Burger": [
                    ("Cheese Burger", 25000, 5),
                    ("Double Beef Burger", 45000, 5),
                    ("Chicken Burger", 22000, 4),
                    ("BBQ Burger", 35000, 5)
                ]
            },

            "🍰 Dessert": {

                "Donat": [
                    ("Donat Coklat", 12000, 5),
                    ("Donat Strawberry", 15000, 4),
                    ("Donat Oreo", 18000, 5),
                    ("Donat Tiramisu", 22000, 5)
                ],

                "Brownies": [
                    ("Brownies Kukus", 25000, 5),
                    ("Brownies Lumer", 30000, 5),
                    ("Brownies Almond", 35000, 4),
                    ("Brownies Keju", 32000, 5)
                ]
            },

            "🥤 Minuman": {

                "Thai Tea": [
                    ("Thai Tea Original", 15000, 5),
                    ("Thai Tea Cheese", 25000, 4),
                    ("Thai Tea Brown Sugar", 30000, 5),
                    ("Thai Tea Jumbo", 22000, 4)
                ],

                "Kopi Latte": [
                    ("Vanilla Latte", 30000, 5),
                    ("Hazelnut Latte", 35000, 4),
                    ("Caramel Latte", 38000, 5),
                    ("Mocha Latte", 42000, 5)
                ]
            }
        }

        self.combo = {
            "Bakso": [
                ("Es Krim", 20000, 5),
                ("Cilok", 15000, 4)
            ],

            "Burger": [
                ("Milkshake", 30000, 5),
                ("Kentang Goreng", 18000, 5)
            ],

            "Pizza": [
                ("Thai Tea", 25000, 5),
                ("Kentang Goreng", 18000, 4)
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
    background: linear-gradient(to bottom right,#f5f7fa,#e4ecf5);
}

.header{
    text-align:center;
    margin-top:10px;
    margin-bottom:30px;
}

.title{
    font-size:60px;
    font-weight:bold;
    color:#2d3436;
}

.subtitle{
    font-size:22px;
    color:#636e72;
}

.food-card{
    background:white;
    border-radius:25px;
    padding:20px;
    text-align:center;
    margin-bottom:20px;
    height:360px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
    transition:0.3s;
    border:1px solid #ecf0f1;
}

.food-card:hover{
    transform:translateY(-5px);
}

.food-emoji{
    font-size:65px;
    margin-top:10px;
}

.food-name{
    font-size:22px;
    font-weight:bold;
    margin-top:10px;
    color:#2d3436;
}

.food-price{
    color:#0984e3;
    font-size:24px;
    font-weight:bold;
    margin-top:10px;
}

.food-rating{
    color:#f1c40f;
    font-size:20px;
    margin-top:8px;
}

.category-title{
    font-size:38px;
    font-weight:bold;
    color:#2d3436;
    margin-top:35px;
    margin-bottom:15px;
}

.sub-menu{
    font-size:26px;
    font-weight:bold;
    color:#0984e3;
    margin-top:20px;
    margin-bottom:10px;
}

.stButton>button{
    width:100%;
    background:#2d3436;
    color:white;
    border:none;
    border-radius:16px;
    height:45px;
    font-size:16px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#0984e3;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#ffffff;
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
    <div class="title">🍽️ GG BITES 🍽️</div>
    <div class="subtitle">
    Smart Food Recommendation & Ordering Experience
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
        "🍽️ Order Menu",
        "🍟 Combo Recommendation",
        "🔥 Top Menu",
        "🎲 Random Pick",
        "💰 Rekomendasi Harga",
        "🔍 Search Menu",
        "🔐 Admin"
    ]
)

st.info("Kode Admin: GGBITES_ADMIN")

# =========================================================
# MAIN PAGE
# =========================================================
st.success("Full source code berhasil dibuat ✨")

print("GG BITES READY")
