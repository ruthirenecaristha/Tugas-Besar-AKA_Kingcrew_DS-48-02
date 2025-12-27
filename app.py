import streamlit as st
import time
import sys
import itertools

# =========================================================
# KONFIGURASI
# =========================================================
sys.setrecursionlimit(20000)
MAX_DISPLAY = 7  # batas aman menampilkan seluruh permutasi

# =========================================================
# FUNGSI FAKTORIAL
# =========================================================
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

# =========================================================
# UI STREAMLIT
# =========================================================
st.set_page_config(page_title="Generator Password", layout="centered")
st.title("🔐 Generator Password (Input Manual)")
st.write(
    "Studi kasus: Menyusun seluruh kemungkinan password "
    "tanpa perulangan karakter dari input pengguna."
)

# =========================================================
# INPUT STRING PASSWORD
# =========================================================
password_base = st.text_input(
    "Masukkan karakter password (tanpa duplikat)",
    value="abcD1"
)

# =========================================================
# BUTTON
# =========================================================
if st.button("🚀 Proses Password"):
    st.divider()

    # =====================================================
    # VALIDASI INPUT
    # =====================================================
    if password_base == "":
        st.error("❌ Password tidak boleh kosong")
        st.stop()

    if len(set(password_base)) != len(password_base):
        st.error("❌ Karakter duplikat terdeteksi! Gunakan karakter unik.")
        st.stop()

    n = len(password_base)

    st.subheader("🔎 Informasi Input")
    st.write(f"Jumlah karakter (n): **{n}**")
    st.code(password_base)

    st.divider()

    # =====================================================
    # 1. PENDEKATAN REKURSIF
    # =====================================================
    st.subheader("1️⃣ Pendekatan Rekursif")

    try:
        start_rec = time.perf_counter()
        hasil_rec = factorial_recursive(n)
        end_rec = time.perf_counter()

        waktu_rec = end_rec - start_rec

        st.success(f"Waktu Eksekusi: {waktu_rec:.10f} detik")
        st.text_area(
            "Total Kemungkinan (Rekursif)",
            value=str(hasil_rec),
            height=70
        )

    except RecursionError:
        st.error("❌ RecursionError (Stack Overflow)")

    st.divider()

    # =====================================================
    # 2. PENDEKATAN ITERATIF
    # =====================================================
    st.subheader("2️⃣ Pendekatan Iteratif")

    start_iter = time.perf_counter()
    hasil_iter = factorial_iterative(n)
    end_iter = time.perf_counter()

    waktu_iter = end_iter - start_iter

    st.success(f"Waktu Eksekusi: {waktu_iter:.10f} detik")
    st.text_area(
        "Total Kemungkinan (Iteratif)",
        value=str(hasil_iter),
        height=70
    )

    st.divider()

    # =====================================================
    # 3. SELURUH PERCOBAAN PASSWORD
    # =====================================================
    st.subheader("3️⃣ Seluruh Percobaan Password")

    if n > MAX_DISPLAY:
        st.warning(
            f"⚠️ Tidak menampilkan seluruh permutasi karena n = {n}\n\n"
            f"Jumlah kemungkinan = {n}! sangat besar dan berisiko membuat aplikasi freeze."
        )
    else:
        start_perm = time.perf_counter()
        perms = list(itertools.permutations(password_base))
        end_perm = time.perf_counter()

        password_list = ["".join(p) for p in perms]

        st.success(f"Total Percobaan: {len(password_list)} password")
        st.caption(f"Waktu Generasi: {end_perm - start_perm:.6f} detik")

        st.text_area(
            "Daftar Seluruh Password",
            value="\n".join(password_list),
            height=300
        )

    st.divider()

    # =====================================================
    # KESIMPULAN
    # =====================================================
    st.info(
        f"📌 Kesimpulan:\n\n"
        f"- Panjang password (n) ditentukan dari input pengguna\n"
        f"- Jumlah kemungkinan = n!\n"
        f"- Pendekatan iteratif lebih stabil\n"
        f"- Enumerasi permutasi memiliki kompleksitas O(n!)"
    )
