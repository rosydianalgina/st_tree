
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="GG BITES",
    page_icon="ðŸ’–",
    layout="wide"
)

if "cart" not in st.session_state:
    st.session_state.cart = []

if "orders" not in st.session_state:
    st.session_state.orders = []

class FoodGraph:

    def __init__(self):
        self.graph = {}

    def add_menu(self, menu):
        if menu not in self.graph:
            self.graph[menu] = []

    def add_recommendation(self, menu1, menu2, weight=1):
        self.add_menu(menu1)
        self.add_menu(menu2)

        self.graph[menu1].append((menu2, weight))
        self.graph[menu2].append((menu1, weight))

    def get_recommendations(self, menu):
        return self.graph.get(menu, [])


foods = [
    {"name": "Bakso", "price": 18000, "emoji": "ðŸœ"},
    {"name": "Burger", "price": 25000, "emoji": "ðŸ”"},
    {"name": "Pizza", "price": 65000, "emoji": "ðŸ•"},
    {"name": "Ayam Geprek", "price": 28000, "emoji": "ðŸ—"},
    {"name": "Kentang Goreng", "price": 18000, "emoji": "ðŸŸ"},
    {"name": "Boba Brown Sugar", "price": 30000, "emoji": "ðŸ§‹"},
    {"name": "Matcha Latte", "price": 35000, "emoji": "ðŸµ"},
    {"name": "Sushi", "price": 30000, "emoji": "ðŸ£"},
]

graph = FoodGraph()

graph.add_recommendation("Bakso", "Matcha Latte", 8)
graph.add_recommendation("Burger", "Kentang Goreng", 10)
graph.add_recommendation("Pizza", "Boba Brown Sugar", 7)
graph.add_recommendation("Sushi", "Matcha Latte", 9)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom right,#fffdfb,#f6f3ef);
    font-family:'Poppins',sans-serif;
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#ff5f99;
}

.sub-title{
    text-align:center;
    color:#666;
    font-size:22px;
    margin-bottom:30px;
}

.food-card{
    background:white;
    padding:20px;
    border-radius:25px;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
}

.top-box{
    background:white;
    padding:20px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,0.05);
}

.stButton > button{
    width:100%;
    border:none;
    border-radius:15px;
    background:linear-gradient(90deg,#ff7eb3,#ff758c);
    color:white;
    font-weight:bold;
}

.cart-box{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
ðŸ’– GG BITES ðŸ’–
</div>

<div class="sub-title">
Smart Food Recommendation & Ordering System
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="top-box"><h3>ðŸœ Menu</h3></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="top-box"><h3>â­ Top Rating</h3></div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="top-box"><h3>ðŸ›’ Cart ({len(st.session_state.cart)})</h3></div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="top-box"><h3>ðŸ” Admin</h3></div>', unsafe_allow_html=True)

st.markdown("## ðŸ½ï¸ Menu Makanan")

cols = st.columns(4)

for i, item in enumerate(foods):

    with cols[i % 4]:

        st.markdown(f"""
        <div class="food-card">
            <h1>{item['emoji']}</h1>
            <h2>{item['name']}</h2>
            <h3 style="color:#ff5f99;">Rp{item['price']:,}</h3>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Tambah {item['name']}", key=item['name']):

            st.session_state.cart.append(item)

            st.success(f"{item['name']} ditambahkan!")

            rekom = graph.get_recommendations(item["name"])

            if rekom:
                st.info("âœ¨ Rekomendasi Menu")

                for r, w in rekom:
                    st.write(f"â€¢ {r} ({w}/10 cocok)")


st.markdown("## ðŸ›’ Keranjang")

st.markdown('<div class="cart-box">', unsafe_allow_html=True)

if len(st.session_state.cart) == 0:

    st.warning("Keranjang masih kosong")

else:

    total = 0

    for item in st.session_state.cart:

        st.write(f"{item['emoji']} {item['name']} - Rp{item['price']:,}")

        total += item["price"]

    st.markdown("---")

    st.subheader(f"ðŸ’° Total: Rp{total:,}")

    payment = st.selectbox(
        "Pilih Pembayaran",
        ["QRIS", "Cash", "DANA", "OVO", "GoPay"]
    )

    customer = st.text_input("Nama Pemesan")

    if st.button("Checkout"):

        if customer == "":

            st.error("Masukkan nama!")

        else:

            order = {
                "customer": customer,
                "items": [x["name"] for x in st.session_state.cart],
                "total": total,
                "payment": payment,
                "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }

            st.session_state.orders.append(order)

            st.success("Pesanan berhasil dibuat!")

            st.session_state.cart = []

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("## ðŸ” Admin Dashboard")

admin_code = st.text_input(
    "Kode Admin",
    type="password"
)

if admin_code == "GGBITES123":

    st.success("Admin berhasil login!")

    if len(st.session_state.orders) == 0:

        st.info("Belum ada pesanan")

    else:

        for i, order in enumerate(st.session_state.orders, start=1):

            st.markdown(f"""
            <div class="cart-box">
                <h3>Order #{i}</h3>
                <p><b>Nama:</b> {order['customer']}</p>
                <p><b>Menu:</b> {', '.join(order['items'])}</p>
                <p><b>Total:</b> Rp{order['total']:,}</p>
                <p><b>Pembayaran:</b> {order['payment']}</p>
                <p><b>Waktu:</b> {order['time']}</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
<br><br>
<center>
ðŸ’– GG BITES Â© 2026
</center>
""", unsafe_allow_html=True)
