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
            "Kentang Goreng": "🍟",
            "Cilok": "🍡",
            "Batagor": "🥟",
            "Donat": "🍩",
            "Brownies": "🧁",
            "Es Krim": "🍦",
            "Thai Tea": "🥤",
            "Boba Brown Sugar": "🧋",
            "Kopi Latte": "☕",
            "Milkshake": "🥛"
        }

        # =====================================================
        # DATA MENU
        # =====================================================
        self.kategori = {

            "🍔 Makanan Berat": {

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
                ]
            },

            "🥤 Minuman": {

                "Thai Tea": [
                    ("Thai Tea Original", 15000),
                    ("Thai Tea Cheese", 25000),
                    ("Thai Tea Brown Sugar", 30000),
                    ("Thai Tea Jumbo", 22000)
                ],

                "Kopi Latte": [
                    ("Vanilla Latte", 30000),
                    ("Hazelnut Latte", 35000),
                    ("Car
