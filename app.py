import streamlit as st


class KategoriNode:
    def  __init__(self, nama_kategori):
        self.nama = nama_kategori
        self.sub_kategori =[] # Ini adalah anak atau cabang dari kategpri

    def tambah_sub(self, node_kategori):
        self.sub_kategori.append(node_kategori)

#mengubah fungsi print menjadi return string agar bisa ditampilkan di web
    def dapatkan_tree_string(self, level=0):
        #mengatur spasi  agar terlihat bertingkat
        indentasi = "    "  *level
        simbol ="↳ " if level > 0 else "📦"
        hasil = f"{indentasi}{simbol}{self.nama}\n"

        for sub in self.sub_kategori:
            hasil += sub.dapatkan_tree_string(level+1)
        return hasil

    def cari_node(self,target_nama):
        #mencari node spesifik untuk menambahkan anak dibawahnya
        if self.nama.lower() == target_nama.lower():
            return self

        for sub in self.sub_kategori:
            hasil =sub.cari_node(target_nama)
            if hasil:
                return hasil
        return None

    def cari_jalur(self, target,path=""):
        #mencari  jalur lengkap (breadcrumb) seperti study kasus sebulumnya
        jalur_saat_ini = path + " > "+ self.nama if path else self.nama

        if self.nama.lower() == target.lower():
            return jalur_saat_ini

        for sub in self.sub_kategori:
            hasil = sub.cari_jalur(target,jalur_saat_ini)
            if hasil : 
                return hasil
        return None

#===========================
#PROGRAM UTAMA 
#===========================


st.set_page_config(page_title ="Struktur Kategori", page_icon= "+")

st.title("Pembuat struktur kategori")
st.write("Aplikasi interaktif untuk mensimulasi struktur data tree")

#inisialisasi session state untuk menyimpan struktur tree agar tidak hilang 
if 'root' not in set.session_state:
    st.session_state.root= None

#jika root belum dibuat, tampilkan form pembuatan root
if st.session_state.root is None:
    st.info("Sistem belum memiliki kategori utama. silakan buat terlebih dahulu.")
    name_root = st.text_input("Masukan nama kategori utama (Root) :", value ="Toko Saya")

    if st.button("Buat kategori utama", type="primary"):
        st.session_state.root = KategoriNode(name_root)
        st.rerun() #refresh halaman

#jika root sudah ada, tampilkan menu utama menggunakan tabs
else:
    root = st.session_state.root

    #mengganti menu cli dengan sistem tab yang lebih moderen
    tab1,tab2,tab3 = st.tabs( [" Lihat struktur", "+ Tambah sub kategori", "Cari Jalur"])

    #TAB 1 ; Lihat struktur
    with tab1:
        st.subheader("Struktur kategori saat ini")
        tree_teks = root.dapatkan_tree_string()
        #Menggunakan st.code agar format identitas (spasi) tetap rapi
        st.code(tree_teks, language="text")

        #tab 2 tambah sub kategori
        with tab2:
            st.subheader("Tambah Cabang Baru")
            induk_nama = st.text_input("Nama kategori induk tempat cabang ditambahkan: ")
            anak_nama = st.text_input("Nama sub-kategori baru:")

            if st.button("Tambah Kategori") :
                if induk_node:
                    induk_node.tambah_sub(KategoriNode(anak_nama))
                    st.success(f"Berhasil menambahkan '{anak_nama}' di bawah' {induk_node.nama}'!")
                else:
                    st.eror(f"Kategori '{induk_nama}' tidak sitemukan! Pastikan Ejaan benar.")

            else:
                st.warning("Harap isi kedua kolom di atas.")

    #tab 3: Cari Jalur 
    with tab3:
        st.subheader("Pencarian Breadcrumb")
        target_cari = st.text_input("Nama kategori yang ingin dicari jalurnya: ")

        if st.button("Cari Jalur"):
            if target_cari:
                hasil = root.cari_jalur(target_cari)
                if hasil:
                    st.success("Ditemukan!")
                    st.info(f" Jalur: {hasil}")
                else:
                    st.eror(f"Kategori '{target_cari}' Tidak ditemukan dalam sistem.")
            else:
                st.warning("Harap isi nama kategori yang dicari.")

#TOMBOL RISET
st.divider()
if st.button("Rise Sistem / Mulai dari awal"):
    st.session_state.root = None
    st.rerun()
    
 
