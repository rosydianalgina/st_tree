import random
class GGBitesGraph:
    def __init__(self):
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
            ],
            "Sate Ayam": [
                ("Sate Ayam Madura", 25000),
                ("Sate Ayam Taichan", 30000),
                ("Sate Ayam Jumbo", 35000),
                ("Sate Ayam Pedas", 28000)
            ],
            "Soto": [
                ("Soto Ayam", 20000),
                ("Soto Lamongan", 25000),
                ("Soto Betawi", 35000),
                ("Soto Daging", 40000)
            ],
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
            ],
            "Sosis Bakar": [
                ("Sosis Bakar Jumbo", 20000),
                ("Sosis Bakar BBQ", 18000),
                ("Sosis Bakar Keju", 25000),
                ("Sosis Bakar Pedas", 22000)
            ],
            "Roti Bakar": [
                ("Roti Bakar Coklat", 18000),
                ("Roti Bakar Keju", 20000),
                ("Roti Bakar Oreo", 25000),
                ("Roti Bakar Tiramisu", 28000)
            ],
            "Siomay": [
                ("Siomay Bandung", 22000),
                ("Siomay Jumbo", 28000),
                ("Siomay Pedas", 25000),
                ("Siomay Seafood", 35000)
            ],
            "Dimsum": [
                ("Dimsum Original", 18000),
                ("Dimsum Chili Oil", 22000),
                ("Dimsum Mentai", 30000),
                ("Dimsum Mozarella", 28000)
            ],
            "Corndog": [
                ("Corndog Mozarella", 25000),
                ("Corndog Sosis", 22000),
                ("Corndog Coklat", 28000),
                ("Corndog Spicy Mayo", 30000)
            ],
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
            ],
            "Cheesecake": [
                ("Cheesecake Oreo", 40000),
                ("Cheesecake Matcha", 50000),
                ("Cheesecake Strawberry", 45000),
                ("Cheesecake Blueberry", 55000)
            ],
            "Waffle": [
                ("Waffle Coklat", 25000),
                ("Waffle Strawberry", 28000),
                ("Waffle Ice Cream", 35000),
                ("Waffle Matcha", 40000)
            ],
            "Pancake": [
                ("Pancake Maple", 25000),
                ("Pancake Coklat", 28000),
                ("Pancake Strawberry", 30000),
                ("Pancake Ice Cream", 38000)
            ],
            "Coklat Dubai": [
                ("Coklat Dubai Mini", 50000),
                ("Coklat Dubai", 250000),
                ("Dubai Chewy Cookie Mini", 25000),
                ("Dubai Chewy Cookie Jumbo", 150000)
            ],
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
            ],
            "Milkshake": [
                ("Chocolate Milkshake", 25000),
                ("Vanilla Milkshake", 28000),
                ("Strawberry Milkshake", 30000),
                ("Oreo Milkshake", 35000)
            ],
            "Es Jeruk": [
                ("Es Jeruk Peras", 12000),
                ("Orange Float", 25000),
                ("Es Jeruk Jumbo", 18000),
                ("Es Jeruk Nipis", 15000)
            ],
            "Lemon Tea": [
                ("Lemon Tea Original", 15000),
                ("Honey Lemon Tea", 25000),
                ("Lychee Lemon Tea", 30000),
                ("Yakult Lemon Tea", 35000)
            ],
            "Matcha Latte": [
                ("Matcha Latte Original", 35000),
                ("Creamy Matcha Latte", 45000),
                ("Premium Matcha Latte", 65000),
                ("Matcha Brown Sugar", 50000)
            ],
            "Yakult": [
                ("Yakult Strawberry", 25000),
                ("Yakult Mango", 28000),
                ("Yakult Lychee", 30000),
                ("Yakult Mix Berry", 35000)
            ]
        }
        # =================================================
        # GRAPH COMBO
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
    # =====================================================
    # FUNGSI BINTANG
    # =====================================================
    def bintang(self, rating):
        return "⭐" * rating
    # =====================================================
    # HEADER
    # =====================================================
    def header(self):
        print("\n╭─ ✧･ﾟ: *✧･ﾟ   GG BITES   ･ﾟ✧*:･ﾟ✧ ─╮")
        print("│  🍽️  Smart Food Recommendation 🍽️   │")
        print("╰─ ✧･ﾟ: *✧･ﾟ･ﾟ✧*:･ﾟ✧ ───────────────╯")
    # =====================================================
    # MENU 1 - LIHAT MENU
    # =====================================================
    def lihat_menu(self):
        print("\n╭──────────〔 📖 DAFTAR MENU 📖 〕──────────╮\n")
        for kategori, daftar_menu in self.kategori.items():
            print(f"🍽️ {kategori}\n")
            for menu in daftar_menu:
                emoji = self.emoji.get(menu, "🍽️")
                print(f"   {emoji} {menu}")
            print()
        print("╰────────────────────────────────────────────╯")
    # =====================================================
    # MENU 2 - CARI REKOMENDASI
    # =====================================================
    def cari_rekomendasi(self):
        print("\n╭──────〔 🔍 CARI REKOMENDASI 🔍 〕──────╮\n")
        for kategori in self.kategori:
            print(f"🍽️ {kategori}")
        kategori_input = input("\n👉 Pilih kategori : ").title()
        if kategori_input not in self.kategori:
            print("\n❌ Kategori tidak ditemukan!")
            return
        print()
        nomor = 1
        for menu in self.kategori[kategori_input]:
            emoji = self.emoji.get(menu, "🍽️")
            print(f"{nomor}. {emoji} {menu}")
            nomor += 1
        pilih = int(input("\n👉 Pilih menu : "))
        menu_pilih = self.kategori[kategori_input][pilih - 1]
        hasil = self.graph_rekomendasi.get(menu_pilih, [])
        print(f"\n╭────〔 ✨ REKOMENDASI {menu_pilih.upper()} ✨ 〕────╮\n")
        nomor = 1
        for menu, harga in hasil:
            print(f"{nomor}. 🍽️ {menu}")
            print(f"   💰 Harga : Rp{harga:,}")
            print()
            nomor += 1
        print("╰──────────────────────────────────────────────╯")
    # =====================================================
    # MENU 3 - FAVORIT HARI INI
    # =====================================================
    def favorit_hari_ini(self):
        semua_menu = []
        for daftar in self.graph_rekomendasi.values():
            semua_menu.extend(daftar)
        pilihan = random.sample(semua_menu, min(5, len(semua_menu)))
        print("\n╭──────〔 🔥 FAVORIT HARI INI 🔥 〕──────╮\n")
        nomor = 1
        for menu, harga in pilihan:
            print(f"{nomor}. 🍽️ {menu}")
            print(f"   💰 Harga : Rp{harga:,}")
            print()
            nomor += 1
        print("╰─────────────────────────────────────────╯")
    # =====================================================
    # MENU 4 - TOP RATING
    # =====================================================
    def top_rating(self):
        top_menu = [
            ("Wagyu Steak", 5),
            ("Pizza Supreme", 5),
            ("Premium Matcha Latte", 5),
            ("Double Beef Burger", 5),
            ("Cheesecake Blueberry", 5)
        ]
        print("\n╭────────〔 🏆 TOP RATING 🏆 〕────────╮\n")
        nomor = 1
        for menu, rating in top_menu:
            print(f"{nomor}. 🍽️ {menu}")
            print(f"   ⭐ Rating : {self.bintang(rating)}")
            print()
            nomor += 1
        print("╰────────────────────────────────────────╯")
    # =====================================================
    # MENU 5 - COMBO RECOMMENDATION
    # =====================================================
    def combo_recommendation(self):
        print("\n╭────〔 💡 COMBO RECOMMENDATION 💡 〕────╮\n")
        nomor = 1
        daftar_menu = list(self.graph_combo.keys())
        for menu in daftar_menu:
            emoji = self.emoji.get(menu, "🍽️")
            print(f"{nomor}. {emoji} {menu}")
            nomor += 1
        pilih = int(input("\n👉 Pilih menu : "))
        menu_dipilih = daftar_menu[pilih - 1]
        hasil = self.graph_combo[menu_dipilih]
        print(f"\n🍽️ {menu_dipilih} cocok dinikmati dengan:\n")
        nomor = 1
        for menu, skor in hasil:
            emoji = self.emoji.get(menu, "🍽️")
            print(f"{nomor}. {emoji} {menu}")
            print(f"   ⭐ Kecocokan : {self.bintang(skor)}")
            print()
            nomor += 1
        print("╰────────────────────────────────────────╯")
    # =====================================================
    # MENU 6 - RANDOM PICK
    # =====================================================
    def random_pick(self):
        semua_menu = []
        for daftar in self.graph_rekomendasi.values():
            semua_menu.extend(daftar)
        pilihan = random.choice(semua_menu)
        print("\n╭──────〔 🎲 RANDOM PICK 🎲 〕──────╮\n")
        print(f"🍽️ {pilihan[0]}")
        print(f"💰 Harga : Rp{pilihan[1]:,}")
        print("\n╰──────────────────────────────────╯")
    # =====================================================
    # MENU 7 - SEARCH MENU
    # =====================================================
    def search_menu(self):
        print("\n╭────────〔 🔎 SEARCH MENU 🔎 〕────────╮")
        keyword = input("\n👉 Cari menu : ").lower()
        ditemukan = False
        print()
        for daftar in self.graph_rekomendasi.values():
            for menu, harga in daftar:
                if keyword in menu.lower():
                    ditemukan = True
                    print(f"🍽️ {menu}")
                    print(f"💰 Harga : Rp{harga:,}")
                    print()
        if not ditemukan:
            print("❌ Menu tidak ditemukan!")
        print("╰────────────────────────────────────────╯")
    # =====================================================
    # MENU 8 - REKOMENDASI BERDASARKAN HARGA
    # =====================================================
    def rekomendasi_harga(self):
        print("\n╭────〔 💰 REKOMENDASI BERDASARKAN HARGA 💰 〕────╮\n")
        print("1. 💸 Murah")
        print("2. 💵 Sedang")
        print("3. 💎 Mahal")
        pilih_harga = input("\n👉 Pilih kategori harga : ")
        if pilih_harga == "1":
            print("\n╭────────〔 💸 MENU TERMURAH 💸 〕────────╮\n")
            nomor = 1
            for kategori, daftar_menu in self.kategori.items():
                menu_termurah = None
                harga_termurah = 999999999
                for menu in daftar_menu:
                    if menu in self.graph_rekomendasi:
                        for nama_menu, harga in self.graph_rekomendasi[menu]:
                            if harga < harga_termurah:
                                harga_termurah = harga
                                menu_termurah = nama_menu
                print(f"{nomor}. 🍽️ {kategori}")
                print(f"   🥘 Menu  : {menu_termurah}")
                print(f"   💰 Harga : Rp{harga_termurah:,}")
                print()
                nomor += 1
        elif pilih_harga == "2":
            print("\n╭────────〔 💵 MENU SEDANG 💵 〕────────╮\n")
            nomor = 1
            for kategori, daftar_menu in self.kategori.items():
                hasil = []
                for menu in daftar_menu:
                    if menu in self.graph_rekomendasi:
                        for nama_menu, harga in self.graph_rekomendasi[menu]:
                            if 25000 < harga <= 50000:
                                hasil.append((nama_menu, harga))
                if len(hasil) > 0:
                    menu_sedang = random.choice(hasil)
                    print(f"{nomor}. 🍽️ {kategori}")
                    print(f"   🥘 Menu  : {menu_sedang[0]}")
                    print(f"   💰 Harga : Rp{menu_sedang[1]:,}")
                    print()
                    nomor += 1
        elif pilih_harga == "3":
            print("\n╭────────〔 💎 MENU TERMAHAL 💎 〕────────╮\n")
            nomor = 1
            for kategori, daftar_menu in self.kategori.items():
                menu_termahal = None
                harga_termahal = 0
                for menu in daftar_menu:
                    if menu in self.graph_rekomendasi:
                        for nama_menu, harga in self.graph_rekomendasi[menu]:
                            if harga > harga_termahal:
                                harga_termahal = harga
                                menu_termahal = nama_menu
                print(f"{nomor}. 🍽️ {kategori}")
                print(f"   🥘 Menu  : {menu_termahal}")
                print(f"   💰 Harga : Rp{harga_termahal:,}")
                print()
                nomor += 1
        else:
            print("\n❌ Pilihan tidak valid!")
    # =====================================================
    # MENU 9 - KELUAR
    # =====================================================
    def keluar(self):
        print("\n╭──────〔 👋 SEE YOU AGAIN 👋 〕──────╮")
        print("      🍽️ Terima kasih telah")
        print("            menggunakan")
        print("             GG BITES")
        print("╰─────────────────────────────────────╯")

app = GGBitesGraph()
# =========================================================
# PROGRAM UTAMA
# =========================================================
while True:
    app.header()
    print("\n╭──────────〔 📋 MENU UTAMA 📋 〕──────────╮\n")
    print("1. 📖 Lihat Menu")
    print("2. 🔍 Cari Rekomendasi")
    print("3. 🔥 Favorit Hari Ini")
    print("4. 🏆 Top Rating")
    print("5. 💡 Combo Recommendation")
    print("6. 🎲 Random Pick")
    print("7. 🔎 Search Menu")
    print("8. 💰 Rekomendasi Berdasarkan Harga")
    print("9. 🚪 Keluar")
    print("\n╰──────────────────────────────────────────╯")
    pilihan = input("\n👉 Pilih menu (1-9): ")
    if pilihan == "1":
        app.lihat_menu()
    elif pilihan == "2":
        app.cari_rekomendasi()
    elif pilihan == "3":
        app.favorit_hari_ini()
    elif pilihan == "4":
        app.top_rating()
    elif pilihan == "5":
        app.combo_recommendation()
    elif pilihan == "6":
        app.random_pick()
    elif pilihan == "7":
        app.search_menu()
    elif pilihan == "8":
        app.rekomendasi_harga()
    elif pilihan == "9":
        app.keluar()
        break
    else:
        print("\n❌ Pilihan tidak valid!")
